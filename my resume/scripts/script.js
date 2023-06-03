var viewResumeButton = document.getElementById("view-resume");
var contactMeButton = document.getElementById("contact-me");
var contactMeButtonFullResume = document.getElementById("contact-me-full-resume");
var fullResumeSection = document.querySelector(".full-resume");
var contactMeModal = document.querySelector(".contact-me");
var closeModal = document.querySelector(".close");
var landingSection = document.querySelector(".landing");

viewResumeButton.addEventListener("click", function() {
	landingSection.style.display = "none";
	fullResumeSection.style.display = "block";
	contactMeModal.style.display = "none";
});

contactMeButton.addEventListener("click", function() {
	landingSection.style.display = "none";
	fullResumeSection.style.display = "none";
	contactMeModal.style.display = "block";
});

contactMeButtonFullResume.addEventListener("click", function() {
	contactMeModal.style.display = "block";
});

closeModal.addEventListener("click", function() {
	contactMeModal.style.display = "none";
});

// Center and position the "Contact Me" button in the middle and bottom of the full resume
var buttonContainerFullResume = document.querySelector(".button-container-full-resume");
var fullResumeHeight = fullResumeSection.offsetHeight;
var windowHeight = window.innerHeight;
var buttonContainerOffset = windowHeight - fullResumeHeight - buttonContainerFullResume.offsetHeight - 50;
buttonContainerFullResume.style.top = buttonContainerOffset + "px";