import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: black;
            color: white;
        }
        #movie-trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        #tvshow-trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #movie-trailer-video {
            width: 100%;
            height: 100%;
        }
        #tvshow-trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #333;
            cursor: pointer;
        }
        .tvshow-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .tvshow-tile:hover {
            background-color: #333;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#movie-trailer-video-container").empty();
        });
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#tvshow-trailer-video-container").empty();
        });
        // Start playing the movie video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var movietrailerYouTubeId = $(this).attr('data-movie-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + movietrailerYouTubeId + '?autoplay=1&html5=1';
            $("#movie-trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'movie-trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Start playing the tvshow video whenever the trailer modal is opened
        $(document).on('click', '.tvshow-tile', function (event) {
            var tvshowtrailerYouTubeId = $(this).attr('data-tvshow-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + tvshowtrailerYouTubeId + '?autoplay=1&html5=1';
            $("#tvshow-trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'tvshow-trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movie content when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Animate in the tvshow content when the page loads
        $(document).ready(function () {
          $('.tvshow-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="movie-trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="movie-trailer-video-container"></div>
        </div>
      </div>
    </div>
    <div class="modal" id="tvshow-trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="tvshow-trailer-video-container"></div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes - Trailers and more!</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <h1><i>Movies</i></h1>{movie_tiles}<h1><i>TV Shows</i></h1>{tvshow_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-movie-trailer-youtube-id="{movie_trailer_youtube_id}" data-toggle="modal" data-target="#movie-trailer">
    <img src="{poster}" width="220" height="342">
    <h2>{movie_title} <small>({movie_year})</small></h2>
    <h4>{movie_plot}</h4>
</div>
'''

# A single tvshow entry html template
tvshow_tile_content = '''
<div class="col-md-6 col-lg-4 tvshow-tile text-center" data-tvshow-trailer-youtube-id="{tvshow_trailer_youtube_id}" data-toggle="modal" data-target="#tvshow-trailer">
    <img src="{poster}" width="220" height="342">
    <h2>{tvshow_title}</h2>
    <h4>{tvshow_plot}</h4>
    <h6>{tvshow_seasons} Seasons - {tvshow_live}</h5>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer)
        movie_trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match
            else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster=movie.poster,
            movie_year=movie.year,
            movie_plot=movie.plot,
            movie_trailer_youtube_id=movie_trailer_youtube_id
        )
    return content


def create_tvshow_tiles_content(tvshows):
    # The HTML content for this section of the page
    content = ''
    for tvshow in tvshows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', tvshow.trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', tvshow.trailer)
        tvshow_trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match
            else None)

        # Append the tile for the tvshow with its content filled in
        content += tvshow_tile_content.format(
            tvshow_title=tvshow.title,
            poster=tvshow.poster,
            tvshow_plot=tvshow.plot,
            tvshow_seasons=tvshow.seasons,
            tvshow_live=tvshow.live,
            tvshow_trailer_youtube_id=tvshow_trailer_youtube_id
        )
    return content


def open_page(movies, tvshows):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        tvshow_tiles=create_tvshow_tiles_content(tvshows))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
