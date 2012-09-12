#!/usr/bin/env python

import sys
import web
from subprocess import *

urls = (  '/', 'index',
          '/test', 'test_internet',
          '/jquery.js', 'jquery')

class test_internet:
  def GET(self):
    output = Popen(["internet"], stdout=PIPE).communicate()[0]
    return output

class jquery:
  def GET(self):
    return open('jquery-1.8.1.min.js', 'r').read()

class index:
  def GET(self):
    html = """
    <html>    
    <body style="background-color: #ccc;">
    <style>
    .text {
      position: relative;
      font-family: "Lucida Grande", "Helvetica Neue", Arial, Helvetica, sans-serif;
      text-align: center;
    }
    .header {
      top: 10%;
      font-size: 25pt;
    }
    .subtext {
      top: 10%;
      font-size: 12pt;
      color: #666;
    }
    #circular3dG{
      position:relative;
      left: 48%;
      top: 10%;
      width:64px;
      height:64px;
    }

    .circular3dG{
      position:absolute;
      background-color:#000000;
      width:18px;
      height:18px;
      -webkit-border-radius:19px;
      -moz-border-radius:19px;
      border-radius:19px;
      -webkit-animation-name:bounce_circular3dG;
      -webkit-animation-duration:1.04s;
      -webkit-animation-iteration-count:infinite;
      -webkit-animation-direction:linear;
      -moz-animation-name:bounce_circular3dG;
      -moz-animation-duration:1.04s;
      -moz-animation-iteration-count:infinite;
      -moz-animation-direction:linear;
      -o-animation-name:bounce_circular3dG;
      -o-animation-duration:1.04s;
      -o-animation-iteration-count:infinite;
      -o-animation-direction:linear;
      -ms-animation-name:bounce_circular3dG;
      -ms-animation-duration:1.04s;
      -ms-animation-iteration-count:infinite;
      -ms-animation-direction:linear;
    }

    #circular3d_1G{
      left:26px;
      top:4px;
      -webkit-animation-delay:0.39s;
      -moz-animation-delay:0.39s;
      -o-animation-delay:0.39s;
      -ms-animation-delay:0.39s}

      #circular3d_2G{
        left:39px;
        top:15px;
        -webkit-animation-delay:0.52s;
        -moz-animation-delay:0.52s;
        -o-animation-delay:0.52s;
        -ms-animation-delay:0.52s;
      }

      #circular3d_3G{
        left:47px;
        top:29px;
        -webkit-animation-delay:0.65s;
        -moz-animation-delay:0.65s;
        -o-animation-delay:0.65s;
        -ms-animation-delay:0.65s;
      }

      #circular3d_4G{
        left:44px;
        top:43px;
        -webkit-animation-delay:0.78s;
        -moz-animation-delay:0.78s;
        -o-animation-delay:0.78s;
        -ms-animation-delay:0.78s}

        #circular3d_5G{
          left:27px;
          top:47px;
          -webkit-animation-delay:0.9099999999999999s;
          -moz-animation-delay:0.9099999999999999s;
          -o-animation-delay:0.9099999999999999s;
          -ms-animation-delay:0.9099999999999999s}

          #circular3d_6G{
            left:5px;
            top:31px;
            -webkit-animation-delay:1.04s;
            -moz-animation-delay:1.04s;
            -o-animation-delay:1.04s;
            -ms-animation-delay:1.04s;
          }

          #circular3d_7G{
            left:0px;
            top:9px;
            -webkit-animation-delay:1.1700000000000002s;
            -moz-animation-delay:1.1700000000000002s;
            -o-animation-delay:1.1700000000000002s;
            -ms-animation-delay:1.1700000000000002s;
          }

          #circular3d_8G{
            left:11px;
            top:0px;
            -webkit-animation-delay:1.3s;
            -moz-animation-delay:1.3s;
            -o-animation-delay:1.3s;
            -ms-animation-delay:1.3s;
          }

          @-webkit-keyframes bounce_circular3dG{
            0%{
              -webkit-transform:scale(1)}

              100%{
                -webkit-transform:scale(.3)}

          }

          @-moz-keyframes bounce_circular3dG{
            0%{
              -moz-transform:scale(1)}

              100%{
                -moz-transform:scale(.3)}

          }

          @-o-keyframes bounce_circular3dG{
            0%{
              -o-transform:scale(1)}

              100%{
                -o-transform:scale(.3)}

          }

          @-ms-keyframes bounce_circular3dG{
            0%{
              -ms-transform:scale(1)}

              100%{
                -ms-transform:scale(.3)}

          }

          </style>
          <p class="text header" id="status">Looking for the internet</p>
          <div id="circular3dG">
          <div id="circular3d_1G" class="circular3dG">
          </div>
          <div id="circular3d_2G" class="circular3dG">
          </div>
          <div id="circular3d_3G" class="circular3dG">
          </div>
          <div id="circular3d_4G" class="circular3dG">
          </div>
          <div id="circular3d_5G" class="circular3dG">
          </div>
          <div id="circular3d_6G" class="circular3dG">
          </div>
          <div id="circular3d_7G" class="circular3dG">
          </div>
          <div id="circular3d_8G" class="circular3dG">
          </div>
          </div>
          <script type='text/javascript' src='jquery.js'></script>
          <script>
            getColor = function(text) {
              var up = /up/;
              var slow = /slow/;
              var down = /down/;

              if (up.test(text)) {
                return 'green';
              } else if (slow.test(text)) {
                return 'yellow';
              } else if (down.test(text)) {
                return 'red';
              } else {
                return 'black';
              }
            }
            updateStatus = function(text) {
              $('#circular3dG').toggle();
              
              lines = text.split('(');
              color = getColor(lines[0]);
              var newHeader = $('#status').replaceWith("<p id='status' style='color: " + color + "; display: none;' class='text header'>" + lines[0] + "</p>");
              var newSubtext = $('#status').after("<p id='subtext' class='text subtext' style='display: none;'>(" + lines[1] + "</p>");
              $('#status').fadeIn();
              $('#subtext').fadeIn();
            };
            $.get('/test',function(data, textStatus, jqXHR) {
              updateStatus(data);
            }, 'text');
          </script>
          </body>
          </html>
          """
    return html

if __name__ == '__main__':
  app = web.application(urls, globals())
  app.run()
