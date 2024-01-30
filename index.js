//get label element with class radio-switch-label for radio-2
const radio1Label = document.querySelector('.radio-switch-label[for="radio-1"]');
const radio2Label = document.querySelector('.radio-switch-label[for="radio-2"]');
const description = document.querySelector('.description');
const pdf = document.querySelector('.pdf');
const canvas = document.getElementById('canvas');


//when radio-2 is clicked, set canvas and description to display "Off"
document.getElementById('radio-2').addEventListener('click', function() {
    canvas.style.display = "none";
    pdf.style.display = "block";
    description.style.display = "none";
});

//when radio-1 is clicked, set canvas display on.
document.getElementById('radio-1').addEventListener('click', function() {
    canvas.style.display = "block";
    pdf.style.display = "none";
    description.style.display = "flex";
});