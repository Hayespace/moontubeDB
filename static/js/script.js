$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

  });
  
  // Convert Video URL
  $(document).ready(function() {
    
    $('#video_link_input').on('input', function() {
        var inputUrl = $(this).val();
        if (isValidYouTubeUrl(inputUrl)) {
            var embedUrl = convertToEmbedUrl(inputUrl);
            $(this).val(embedUrl);
        }
    });

    // Function to check if a URL is a valid YouTube URL
    function isValidYouTubeUrl(url) {
        return url.includes('youtube.com');
    }

    // Function to convert a YouTube URL to the embed format
    function convertToEmbedUrl(url) {
        var videoId = getVideoIdFromUrl(url);
        if (videoId) {
            return 'https://www.youtube.com/embed/' + videoId;
        }
        return url;
    }

    // Function to extract the video ID from a YouTube URL
    function getVideoIdFromUrl(url) {
        var match = url.match(/[?&]v=([^&]+)/);
        return match ? match[1] : null;
    }
});

// Function to update video preview based on user input
function updateVideoPreview() {
    const videoLinkInput = document.getElementById('video_link_input');
    const videoPreview = document.getElementById('video-preview');
    const videoId = getYouTubeVideoId(videoLinkInput.value);

    if (videoId) {
        // Construct the embedded YouTube iframe
        const iframeHtml = `<iframe width="560" height="315" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>`;
        videoPreview.innerHTML = iframeHtml;
    } else {
        // Clear the preview if no valid video ID is found
        videoPreview.innerHTML = '';
    }
}
// Function to extract YouTube video ID from URL
function getYouTubeVideoId(url) {
    const match = url.match(/[?&]v=([^&]+)/);
    return match && match[1];
}

   // Function to display a video preview
   function displayVideoPreview() {
    var videoLink = $("#video_link_input").val();
    
    // Check if the input contains a valid YouTube URL
    if (videoLink.includes("youtube.com")) {
        // Extract the video ID from the URL
        var videoID = videoLink.split("v=")[1];
        
        // Embed the video using an iframe
        var embedCode = '<iframe width="560" height="315" src="https://www.youtube.com/embed/' + videoID + '" frameborder="0" allowfullscreen></iframe>';
        
        // Display the video preview
        $("#video-preview").html(embedCode);
    } else {
        // Invalid or unsupported URL
        $("#video-preview").html("Invalid or unsupported video URL");
    }
}

// Bind the function to the input field's change event
$("#video_link_input").on("input", function() {
    displayVideoPreview();
});






  