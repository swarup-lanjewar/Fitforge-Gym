function calculateBMI() {

    let h = document.getElementById('height').value / 100;
    let w = document.getElementById('weight').value;

    if (!h || !w) {
        document.getElementById("result").innerHTML =
            "Please enter height and weight";
        return;
    }

    let bmi = w / (h * h);

    document.getElementById("result").innerHTML =
        "Your BMI: " + bmi.toFixed(1);
}


/* AJAX FORMS */

document.addEventListener("DOMContentLoaded", () => {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", async (e) => {

            e.preventDefault();

            const formData = new FormData(form);

            try {

                const response = await fetch(
                    form.action,
                    {
                        method: "POST",
                        body: formData
                    }
                );

                const data = await response.json();

                alert(data.message);

                form.reset();

            }

            catch(error) {

                alert("Something went wrong!");

            }

        });

    });

});