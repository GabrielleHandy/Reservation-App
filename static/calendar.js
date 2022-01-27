


const searchForm = document.querySelector('#search');
const resultBox = document.querySelector('#available');
searchForm.addEventListener('submit', evt => {
    evt.preventDefault();
    resultBox.innerHTML == "Searching for available times...";


    const minTime = document.querySelector('#min-time').value;
    const maxTime = document.querySelector('#max-time').value;
    const desiredDate = document.querySelector('#date').value;

    const params = {'min-time': minTime,
                    'max-time': maxTime,
                    'input-date': desiredDate};
        const options = {
        method: 'POST',
        body: JSON.stringify( params ),  
        headers: {
            'Content-Type': 'application/json'
                }
        };

        fetch('/reservation_options', options)
        .then(data => data.json())
        
        .then(times => showTimes(times, desiredDate))



});

function showTimes(times, inputDate){
    resultBox.innerHTML = "";

    if (times === []){
        resultBox.innerHTML == "Sorry, there aren't any available times";
    }
    else if (times === 'You already have a melontastic tasting on this day!'){
        resultBox.innerHTML =  '<h1> You already have a melontastic tasting on this day!</h1>';
    }
    else{
        resultBox.insertAdjacentHTML('beforeend', "<h3>Here is what's available</h3>");
        resultBox.insertAdjacentHTML('beforeend', '<ul id="resultList"></ul>');
        const resultList = document.querySelector('#resultList');
        for(let time of times){
            resultList.insertAdjacentHTML('beforeend', `<ol>${time}  <button onclick="makeReservation('${inputDate}', '${time}' );">Reserve this time!</button></ol>`);
        }
    }
};

function makeReservation(inputDate, time){

    const param = {'inputDate': inputDate,
                    'inputTime': time
                    };
        const options = {
        method: 'POST',
        body: JSON.stringify( param ),  
        headers: {
            'Content-Type': 'application/json'
                }
        };

        fetch('/create_reservation', options)
        .then(data => data.json())
        
        .then(message => sendAlert(message))
    
       

};

function sendAlert(msg){
    location.reload();

    alert(msg);
    
    
    

};