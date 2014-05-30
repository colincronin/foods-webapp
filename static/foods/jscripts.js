function enterFunction(event, input_id, input) {
    if(event.keyCode == 13) {
        myFunction(input_id, input);
    }
}
function myFunction(input_id, input) {
    if (input % 1 == 0 && input != '') {
        output = input/100;
        document.getElementById(input_id).value = output;
    }
}
