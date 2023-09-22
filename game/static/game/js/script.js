var countElement = document.getElementById('count');
var count = parseInt(countElement.innerText);

function updateCount() {
    count--;
    countElement.innerText = count;

    if (count <= 0) {
        clearInterval(interval);
        window.location.href = '/';
    }
}

var interval = setInterval(updateCount, 100000);
var modal = document.getElementById("myModal");
var openModalBtn = document.getElementById("openModalBtn");
var closeModalBtn = document.getElementById("closeModalBtn");

openModalBtn.onclick = function() {
    modal.style.display = "block";
}

closeModalBtn.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
