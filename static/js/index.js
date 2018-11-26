/*global $*/

$(document).ready(function() {

    var write = document.getElementById("questions");
    var questions = [];

    //Get Data Function
    function getData(callback) {
        $.get("/getQuestions", function(response) {
            var data = JSON.stringify(response)
            callback(data);
        });
    };

    //Initial Loading Information
    function load() {

        var results = [];

        getData(function(response) {
            questions.push(response);

            questions.forEach(function(entry) {
                results.push(`
                       <div class="row">
                            <div class="col-md-12">
                                 <h2>What does this word mean: ${entry.Spanish} ?</h2>
                                 <button id="test" class="btn btn-primary">Test</button>
                            </div>
                       </div>
                `);
            });
            write.innerHTML = results.join('');

        });

    };

    //Load the Data on Page Load
    load();

})
