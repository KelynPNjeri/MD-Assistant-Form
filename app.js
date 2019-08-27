const baseURL = 'https://medical-diagnostics.herokuapp.com/disease/';
let disease_name = document.getElementById("disease-name").value;
let disease_signs = document.getElementById("disease-signs").value;
let disease_symptoms = document.getElementById("disease-symptoms").value;
let confirmatory_tests = document.getElementById("confirmatory-tests").value;

const addDiseaseInfo = () => {
    
    const disease_name = document.getElementById('disease-name').value;
    const disease_signs = document.getElementById('disease-signs').value;
    const disease_symptoms = document.getElementById('disease-symptoms').value;
    const confirmatory_tests = document.getElementById('confirmatory-tests').value;
    const baseURL = 'https://medical-diagnostics.herokuapp.com/disease/';

    fetch(baseURL, {
        method:'POST',
        headers: {
            'Accept': 'application/json',
            'Content-type':'application/json',
        },
        body:JSON.stringify({
            "disease_name": disease_name, 
            "disease_signs": disease_signs, 
            "disease_symptoms": disease_symptoms, 
            "confirmatory_tests": confirmatory_tests 
        })
    }).then( 
        resp => resp.json(). then( data => { 
            console.log(data);
            document.getElementById('diseases-info').reset();
    }))
}
