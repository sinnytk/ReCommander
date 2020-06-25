$(document).ready(function () {
  const user_input = $("#user-input");
  const search_icon = $("#search-icon");
  const movie_section = $("#movieSection");
  const endpoint = "/search";
  const delay_by_in_ms = 700;
  let scheduled_function = false;
  let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
      .done((response) => {
        // fade out the movie_section, then:
        movie_section.fadeTo("slow", 0).promise().then(() => {
          // replace the HTML contents
          movie_section.html(response["html_from_view"]);
          // fade-in the div with new contents
          movie_section.fadeTo("slow", 1);
          // stop animating search icon
          search_icon.removeClass("blink");
        });
      });
  };
  user_input.keyup(function () {
    const request_parameters = {
      query: $(this).val(), // value of user_input: the HTML element with ID user-input
    };

    // start animating the search icon with the CSS class
    search_icon.addClass("blink");

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
      clearTimeout(scheduled_function);
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(
      ajax_call,
      delay_by_in_ms,
      endpoint,
      request_parameters,
    );
  });
  $('#movieSection').on("click", ".movie", function () {
    var selected_movie = $(this).attr('data-movie-id');
    $('#selected-movie').val(selected_movie)
    $('#movie-form').submit()
  })
});
