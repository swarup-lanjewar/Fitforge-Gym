function calculateBMI() {

    let h = document.getElementById('height').value / 100;
    let w = document.getElementById('weight').value;

    if (!h || !w) {
        document.getElementById('result').innerHTML =
            "Please enter height and weight";
        return;
    }

    let bmi = w / (h * h);

    document.getElementById('result').innerHTML =
        'Your BMI: ' + bmi.toFixed(1);

}