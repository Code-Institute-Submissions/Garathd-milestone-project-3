/*global $*/

$(document).ready(function() {

    var questions = [];
    var writing = document.getElementById("questions");
    

    function searchList(callback) {
        var array = [];
        $.getJSON(`https://api.myjson.com/bins/127waa`, function(data) {
            $.each(data, function(index, value) {
                array.push(value);
            });
            callback(array);
        });
    };

    function getQuestions() {
        searchList(function(response) {
            response.forEach(function(entry) {
                questions.push(`
                <div class="row">
                 <div class="col-md-12">
                     <h2>What is the meaning of: ${entry.Spanish}?</h2>
                     <ul>
                         <l1><label><p>Its : ${entry.English}</p></label></l1>
                     </ul>
                 </div> 
                </div>
                `);
            });
        
            writing.innerHTML = questions.join('');
        });
    };





    //Initialise
    getQuestions();


})
