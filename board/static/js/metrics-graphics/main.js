'use strict';

$(document).ready(function() {
    //json data that we intend to update later on via on-screen controls
    var wa, mrta, mrtw;

    var torso = {};
    torso.width = 500;
    torso.height = 200;
    torso.right = 20;

    var trunk = {};
    trunk.width = 320;
    trunk.height = 150;
    trunk.left = 35;
    trunk.right = 10;
    trunk.xax_count = 5;

    var small = {};
    small.width = 240;
    small.height = 140;
    small.left = 20;
    small.right = 20;
    small.top = 20;
    small.xax_count = 5;

    assignEventListeners();

    d3.json('/static/data/response_time_web.json', function(response_time_web) {
        response_time_web = convert_dates(response_time_web, 'date');
    d3.json('/static/data/response_time_api.json', function(response_time_api) {
        response_time_api = convert_dates(response_time_api, 'date');
    d3.json('/static/data/uptime.json', function(uptime) {
        uptime = convert_dates(uptime, 'date');

        // var markers = [{
        //     'date': new Date('2014-02-01T00:00:00.000Z'),
        //     'label': '1st Milestone'
        // }, {
        //     'date': new Date('2014-03-15T00:00:00.000Z'),
        //     'label': '2nd Milestone'
        // }]

        wa = moz_chart({
            title: "Website Availability",
            description: "Here is an example that shows percentages.",
            data: uptime,
            width: torso.width*2,
            height: torso.height,
            right: torso.right,
            transition_on_update: false,
            // markers: markers,
            format: 'percentage',
            target: '#metric1',
            x_accessor: 'date',
            y_accessor: 'value'
        });
        moz_chart({
            title: "Website Availability",
            description: "Here is an example that shows percentages.",
            data: modify_time_period(wa, 2),
            width: torso.width*2,
            height: torso.height,
            right: torso.right,
            transition_on_update: false,
            // markers: markers,
            format: 'percentage',
            target: '#metric1',
            x_accessor: 'date',
            y_accessor: 'value'
        });

        mrta = moz_chart({
            title: "Mean Request Time (API)",
            description: "Fill me in for a layman's description of this metric.",
            data: response_time_api,
            linked: true,
            width: torso.width*2,
            height: trunk.height,
            right: trunk.right,
            transition_on_update: false,
            show_years: false,
            xax_count: 4,
            target: '#metric2',
            x_accessor: 'date',
            y_accessor: 'value'
        });
        moz_chart({
            title: "Mean Request Time (API)",
            description: "Fill me in for a layman's description of this metric.",
            data: modify_time_period(mrta, 2),
            linked: true,
            width: torso.width*2,
            height: trunk.height,
            right: trunk.right,
            transition_on_update: false,
            show_years: false,
            xax_count: 4,
            target: '#metric2',
            x_accessor: 'date',
            y_accessor: 'value'
        });

        mrtw = moz_chart({
            title: "Mean Request Time (Web Page)",
            description: "The chart is gracefully updated depending on the chosen time period.",
            data: response_time_web,
            linked: true,
            width: torso.width*2,
            height: trunk.height,
            right: trunk.right,
            transition_on_update: false,
            show_years: false,
            xax_count: 4,
            target: '#metric3',
            x_accessor: 'date',
            y_accessor: 'value'
        });
        moz_chart({
            title: "Mean Request Time (Web Page)",
            description: "The chart is gracefully updated depending on the chosen time period.",
            data: modify_time_period(mrtw, 2),
            linked: true,
            width: torso.width*2,
            height: trunk.height,
            right: trunk.right,
            transition_on_update: false,
            show_years: false,
            xax_count: 4,
            target: '#metric3',
            x_accessor: 'date',
            y_accessor: 'value'
        });

        $('.line1-color').css('stroke', '#4090c4');
        $('.line1-legend-color').css('stroke', '#4040e8');
        $('.area1-color').css('fill', '#4090f4');
    });
    });
    });

    function assignEventListeners() {
        $('.modify-time-period-controls button').click(function() {
            var past_n_days = $(this).data('time_period');
            var u1 = modify_time_period(wa, past_n_days);
            var u2 = modify_time_period(mrta, past_n_days);
            var u3 = modify_time_period(mrtw, past_n_days);

            //change button state
            $(this).addClass('active')
                .siblings()
                .removeClass('active');

            moz_chart({
                title: "Website Availability",
                description: "Here is an example that shows percentages.",
                data: u1,
                width: torso.width * 2,
                height: torso.height,
                right: torso.right,
                transition_on_update: false,
                // markers: markers,
                format: 'percentage',
                target: '#metric1',
                x_accessor: 'date',
                y_accessor: 'value'
            });

            //update data
            moz_chart({
                data: u2,
                width: torso.width*2,
                height: trunk.height,
                right: trunk.right,
                show_years: false,
                transition_on_update: false,
                xax_count: 4,
                target: '#metric2',
                x_accessor: 'date',
                y_accessor: 'value'
            });

            moz_chart({
                data: u3,
                width: torso.width*2,
                height: trunk.height,
                right: trunk.right,
                show_years: false,
                transition_on_update: false,
                xax_count: 4,
                target: '#metric3',
                x_accessor: 'date',
                y_accessor: 'value'
            });

        });
    }

    //replace all SVG images with inline SVG
    //http://stackoverflow.com/questions/11978995/how-to-change-color-of-svg
    //-image-using-css-jquery-svg-image-replacement
    $('img.svg').each(function() {
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');

        $.get(imgURL, function(data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Add replaced image's ID to the new SVG
            if(typeof imgID !== 'undefined') {
                $svg = $svg.attr('id', imgID);
            }
            // Add replaced image's classes to the new SVG
            if(typeof imgClass !== 'undefined') {
                $svg = $svg.attr('class', imgClass+' replaced-svg');
            }

            // Remove any invalid XML tags as per http://validator.w3.org
            $svg = $svg.removeAttr('xmlns:a');

            // Replace image with new SVG
            $img.replaceWith($svg);

        }, 'xml');
    });
});
