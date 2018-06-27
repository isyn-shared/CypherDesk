$("#message_title").keyup(() => {

    $.ajax({
        type: "GET",
        url: "found_titles/",

        data: {
            'message_title': $("#message_title").val(),
        },

        dataType: "text",
        cache: false,

        success: data => {
            let titles = data.split("~");
            let result = "";

            for (let i = 0; i < titles.length; i++)
                if (titles[i] != "" && titles[i] != " ")
                    result += `<h5>Title ${i + 1} : ${titles[i]}</h5>`;

            $("div.hint_titles").html(result);
        }
    });
});