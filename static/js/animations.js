document.addEventListener("DOMContentLoaded", function () {
    const calendarInputs = document.querySelectorAll(".calendar-widget");
    calendarInputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.backgroundColor = "#f0fff0";
        });
        input.addEventListener("blur", () => {
            input.style.backgroundColor = "white";
        });
    });
});
