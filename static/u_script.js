var optionForEachQuestion = [];
var i, len;
var questionNumber = 1;
var optionNumber = 2;
$(document).ready(function() {
    $('.addOption').click(function() {
        option = document.getElementById('options' + questionNumber);
        // console.log(option)
        if (optionNumber == 5) {
            alert("Too many options");
            return false;
        }
        $(option).append("<div class='row'><div class='input-field col s6' id='o" + questionNumber + optionNumber + "'><label for='t" + questionNumber + optionNumber + "'>Option " + optionNumber + "</label><input type='text' id='t" + questionNumber + optionNumber + "'></div></div>");

        console.log("<div class='row'><div class='input-field col s6' id='o" + questionNumber + optionNumber + "'><label for='t" + questionNumber + optionNumber + "'>Option " + optionNumber + "</label><input type='text' id='t" + questionNumber + optionNumber + "'></div></div>")
        optionNumber++;
        addQ = document.getElementById('main');
        // console.log(addQ);
    });
    $('.removeOption').click(function() {
        if (optionNumber == 1) {
            alert("Please add some options to remove:)");
            return false;
        }
        --optionNumber;
        removeOption = document.getElementById('o' + questionNumber + optionNumber);
        $(removeOption).remove();

    });

    $('#addQuestion').click(function() {
        // $('#Question'+questionNumber).find('a').remove();
        optionForEachQuestion.push(optionNumber - 1);
        questionNumber++;
        optionNumber = 1;
        addQ = document.getElementById('main');
        $(addQ).append("<div class='container inside' id='Question" + questionNumber + "'><div class='container'><div class='row'><div class='input-field col s12'><textarea id='question" + questionNumber + "' class='materialize-textarea'></textarea><label for='question" + questionNumber + "'>Question " + questionNumber + " </label></div>" +

            "<form id='options" + questionNumber + "'><div class='row' id='o" + questionNumber +
            "1'><div class='input-field col s6'><label for='t" + questionNumber + optionNumber + "'>Option 1</label><input type='text' id='t" + questionNumber + optionNumber + "'></div></div></form>"

            +"<form id='correctoption"+questionNumber+"'><div class='row' id='co"+questionNumber+"'><div class='input-field col s8'><label for='Col"+questionNumber
            +"'> Correct Option Number for Question "+questionNumber+"</label><input type='text' id='Co1'></div></div></form>"+
            "</div></div></div>"
        );
                     
        optionNumber++;
        // console.log(addQ);
        len = optionForEachQuestion.length
        for (i = 0; i < len; i++) {
            console.log(optionForEachQuestion[i]);
        }


    });
    $('#removeQuestion').click(function() {
        if (questionNumber == 0) {
            alert("Please add some questions to remove");
            return false;
        }

        removeQuestion = document.getElementById('Question' + questionNumber);
        $(removeQuestion).remove();
        optionForEachQuestion.pop();
        questionNumber--;

    });

});