
// var url = 'https://www.youtube.com/watch?v=I13u8Ll8jfc'

var url = 'https://youtu.be/YVSRQwItv08'

videoid = youTubeIdFromURL(url)

function youTubeIdFromURL(url){
    var videoid = url.match(/(?:https?:\/{2})?(?:w{3}\.)?youtu(?:be)?\.(?:com|be)(?:\/watch\?v=|\/)([^\s&]+)/);        
    
    if(videoid != null) {
        console.log("video id = ",videoid[1]);
        return videoid = videoid[1].toString()
    } else { 
        console.log("The youtube url is not valid.");
        return -1
    }
}


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
    events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
}
    

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    event.target.stopVideo
}
    
    
// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
      setTimeout(stopVideo, 4000);
      // done = true;
    }
}    

function stopVideo() {
    player.stopVideo();
}
    
    
function loopVideo() {  
    player.seekTo(30);
    player.playVideo()
}    



