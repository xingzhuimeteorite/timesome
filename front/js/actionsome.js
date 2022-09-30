var imagesize = 220;
var linesize = 1000;
var url = "http://208.87.133.114:5000/static/shanshan/"
function lineMove(linesize, imagsize, wsize) {
  var elem = document.getElementById("line");
  var pos = 0;
  var id = setInterval(frame, 5);
  function stepadd() {
    pos++;
    console.log("hello");
    elem.style.height = pos + "px";
  }
  function frame() {
    if (pos == imagsize) {
      cline1Move("cline0", pos, wsize);
      displayimg("begin");
    }
    if (pos % imagsize == 0 && pos > imagsize) {
      num = pos / imagsize
      clineid = "cline" + num;
      addcline("line", clineid);
      if (num % 2 == 0) {
        cline2Move(clineid, pos, wsize);

      } else {
        cline1Move(clineid, pos, wsize);
      }
      imgid = "img" + num;
      clinedit(clineid, url + num + ".jpg", imgid);
      displayimg(imgid);
    }
    if (pos == linesize) {
      clearInterval(id);
    }
    else {
      stepadd();
      movehtml(pos);
    }
  }
}

function cline1Move(id, tpos, size) {
  var elem = document.getElementById(id);
  var pos = 0;
  elem.style.top = tpos + "px";
  var id = setInterval(frame1, 6);
  function frame1() {
    if (pos == size) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.width = pos + "px";
    }
  }
}

function cline2Move(id, tpos, size) {
  var elem = document.getElementById(id);
  var pos = 0;
  var left = 0;
  elem.style.top = tpos + "px";
  elem.style.backgroundColor = "pink";
  var id = setInterval(frame2, 6);
  function frame2() {
    if (pos == size) {
      clearInterval(id);
    } else {
      pos++;
      left--;
      elem.style.width = pos + "px";
      elem.style.left = left + "px";

    }
  }
}
function displayimg(id) {
  var elem = document.getElementById(id);
  elem.style.display = "block"
}
function addcline(id, childid) {
  var elem = document.getElementById(id);
  var newdiv = document.createElement("div");
  newdiv.setAttribute("class", "cline");
  newdiv.setAttribute("id", childid);
  elem.appendChild(newdiv);
}
function movehtml(tpos) {
  window.scrollBy(0, tpos);
}
function clinedit(id, url, imgid) {
  var cline = document.getElementById(id);
  var aurl = document.createElement("img");
  aurl.setAttribute("src", "data:" + url + ";base64");
  aurl.setAttribute("id", imgid);
  cline.appendChild(aurl);
}
setTimeout(1000);
lineMove(linesize, imagesize / 2 + 10, imagesize + 20);