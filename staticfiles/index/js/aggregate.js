function calculate_aggregate() {
    var total_points = 0;
    var jamb_score = document.getElementById('jamb_score').value;

    var grade_map = {
        'A1': 10,
        'B2': 9,
        'B3': 8,
        'C4': 7,
        'C5': 6,
        'C6': 5
    };

    var num_1 = document.getElementById('sub_one').value;
    var num_2 = document.getElementById('sub_two').value;
    var num_3 = document.getElementById('sub_three').value;
    var num_4 = document.getElementById('sub_four').value;
    var num_5 = document.getElementById('sub_five').value;

    var grade_list = [num_1, num_2, num_3, num_4, num_5];

    for (var i = 0; i < 5; i++) {
        if (grade_list[i] == "grade"){
            alert('Invalid grade input. Check and try again!');
            break;
        }
        total_points += parseFloat(grade_map[grade_list[i]]);
    }

    if ((parseFloat(jamb_score) > 400) | (jamb_score < 0)) {
        alert('Invalid JAMB Score!');
    } else {
        var aggregate = parseFloat(total_points) + parseFloat(jamb_score / 8);

        document.getElementById('sub_but').innerText = 'AGGREGATE: ' + aggregate.toFixed(2);
        document.getElementById('o-level').innerText = 'O-LEVEL POINT: ' + total_points;
        document.getElementById('utme').innerText = 'UTME POINT: ' + parseFloat(jamb_score / 8).toFixed(2);
        document.getElementById('aggregate').innerText = 'TOTAL AGGREGATE SCORE: ' + aggregate.toFixed(2);
    }

}