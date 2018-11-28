/*global $*/

$(document).ready(function() {

    var questions = [];
    var writing = document.getElementById("questions");


    function randomNumber(limit, callback) {
        var array = [];
        var min = 0;
        for (var i = 0; i < 4; i++) {
            var result = parseInt(Math.random() * (limit - min) + min);

            for (var a = 0; a < array.length; a++) {
                if (result === a.length) {
                    array.splice(a, 1);
                }
            }

            array.push(result);
        }
        callback(array);
    };


    function searchList(callback) {
        var array = [];
        $.getJSON(`https://api.myjson.com/bins/127waa`, function(data) {
            $.each(data, function(index, value) {
                array.push(value);
            });
            callback(array);
        });
    };

    //Get the Questions
    function getQuestions() {
        searchList(function(response) {

            //Random Number Generation
            var limit = response.length;
            console.log("limit: " + limit);
            randomNumber(limit, function(numbers) {
                console.log("The random number is: " + numbers);

                questions.push(`
                <div class="row">
                 <div class="col-md-12">
                     <h2>What is the meaning of: ${response[0].Spanish}?</h2>
                     <hr />
                     <p>Choose one of the following:</p>
                     <ul>
                         <l1><label><button class="btn btn-primary">${response[numbers[0]].English}</button></label></l1>
                         <l1><label><button class="btn btn-primary">${response[numbers[1]].English}</button></label></l1>
                         <l1><label><button class="btn btn-primary">${response[numbers[2]].English}</button></label></l1>
                         <l1><label><button class="btn btn-primary">${response[numbers[3]].English}</button></label></l1>
                     </ul>
                 </div> 
                </div>
                `);

                writing.innerHTML = questions.join('');

            });

        });
    };





    //Initialise
    getQuestions();


})
