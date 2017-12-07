
// -----------------------------------------------------------------------------
// YouTube JS

var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
    
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.

var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: videoid,
    playerVars: {rel: 0, 'controls': 0},
    events: {
        'onReady': initialize,
        'onStateChange': onPlayerStateChange
      }
    });
}
    

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    event.target.stopVideo
}

// -----------------------------------------------------------------------------

var time_update_interval
function initialize(){

    // Update the controls on load
    updateTimerDisplay();
    updateProgressBar();

    // Clear any old interval.
    clearInterval(time_update_interval);

    // Start interval to update elapsed time display and
    // the elapsed part of the progress bar every second.
    time_update_interval = setInterval(function () {
        checkLoopStatus();
        updateTimerDisplay();
        updateProgressBar();
    }, 1000)

}

function checkLoopStatus() {
    var loop = document.getElementById('snippet_loop').checked;
    var start = parseFloat(document.getElementById('id_start').value);
    var end = parseFloat(document.getElementById('id_end').value);
    var current = (player.getCurrentTime());
    
    if (loop) {
        if (end <= start) {
            // error message
            document.getElementById('snippet_loop').checked = false
        } else if (current >= end){
            player.seekTo(start)
        }
    }
}

function updateTimerDisplay(){
    // Update current time text display.
    
    $('#current-time').text( Number((player.getCurrentTime()).toFixed(0)) );
    $('#duration').text(formatTime( player.getDuration() ));
}

function formatTime(time){
    time = Math.round(time);

    var minutes = Math.floor(time / 60),
    seconds = time - minutes * 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;

    return minutes + ":" + seconds;
}

// This function is called by initialize()
function updateProgressBar(){
    // Update the value of our progress bar accordingly.
    $('#progress-bar').val((player.getCurrentTime() / player.getDuration()) * 100);
}

function resetProgressBar(){
    // Reset the progress bar to the beginning
    $('#progress-bar').val(0);
}

$('#progress-bar').on('mouseup touchend', function (e) {

    // Calculate the new time for the video.
    // new time in seconds = total duration in seconds * ( value of range input / 100 )
    var newTime = player.getDuration() * (e.target.value / 100);

    // Skip video to new time.
    player.seekTo(newTime);

});

    
// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
    // if (event.data == YT.PlayerState.PLAYING && !done) {
    //   setTimeout(stopVideo, 4000);
      // done = true;
    // }
}    

// -----------------------------------------------------------------------------
// Functions

function pauseVideo() {
    var current = player.getCurrentTime()
    player.pauseVideo();
    player.seekTo(current);
}

function playSnippet() {
    var start = parseFloat(document.getElementById('id_start').value)
    var current = player.getCurrentTime()
    if (current > start){
        player.seekTo(current);
    }else{
        player.seekTo(start);
    }
    player.playVideo()
}

function jumpBack(){
    var seconds = parseFloat(document.getElementById('id_jump').value)
    console.log(seconds)
    var current, back;
    current = player.getCurrentTime()
    if (current - seconds >= 0) {
        back = current - seconds;
        player.seekTo(back);
    }
}    

function playRestart(){
    var start = parseFloat(document.getElementById('id_start').value)
    player.seekTo(start);
}

function setMarker(type) {
    // var start = parseFloat(document.getElementById('id_start').value)
    // var end = parseFloat(document.getElementById('id_end').value)
    var current = Number((player.getCurrentTime()).toFixed(1));
    var tag;
    if (type == 0){
        tag = document.getElementById('id_start')
    }else{
        tag = document.getElementById('id_end')
    }
    tag.value = current
}

function setSpeed(val) {
    player.setPlaybackRate(val)
}

// -----------------------------------------------------------------------------
// Button Toggle

$('#play_btn').click(function(){
    var $this = $(this);
    $this.toggleClass('tmp');
    if($this.hasClass('tmp')){
        $this.text('Pause'); 
        $this.onclick=playSnippet()
    } else {
        $this.text('Play');
        $this.onclick=pauseVideo()
    }
});


