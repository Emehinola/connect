jQuery(document).ready(function () {
    "use scripts";

    $('#sub_one').change(
        function () {
            // console.log(
            //     $(this).find('option:selected').attr('value')
            // );

            var course = $(this).find('option:selected').attr('value');

            $.ajax({
                url: '/course-selector/get-course/',
                dataType: 'json',
                method: 'GET',
                contentType: 'application/json',
                data: {
                    'course': course
                },
                success: function (data, status, xhr) {
                    console.log(data['no_of_views'])

                    $('#olevel').text(data['olevel']);
                    $('#jamb').html(data['jamb']);
                    $('#desc').html(data['desc']);
                    $('#views').html(data['no_of_views']);

                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    )

});