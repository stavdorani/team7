
          $(document).ready(function () {
            
                            $('.star').click(function () {
                    if ($(this).hasClass("InstructorPerformance")) {
                        $('#InstructorPerformance').val('' + $(this).prop("id") + '')
                        type = "InstructorPerformance";
                        value = $(this).prop("id");
                    }
                    else if ($(this).hasClass("CourseContent")) {
                        $('#CourseContent').val('' + $(this).prop("id") + '')
                        type = "CourseContent";
                        value = $(this).prop("id");
                    }
                    else if ($(this).hasClass("CourseTime")) {
                        $('#CourseTime').val('' + $(this).prop("id") + '')
                        type = "CourseTime";
                        value = $(this).prop("id");
                    }
                    else if ($(this).hasClass("OutcomesAchieve")) {
                        $('#OutcomesAchieve').val('' + $(this).prop("id") + '')
                        type = "OutcomesAchieve";
                        value = $(this).prop("id");
                    }
                    else if ($(this).hasClass("CourseDuration")) {
                        $('#CourseDuration').val('' + $(this).prop("id") + '')
                        type = "CourseDuration";
                        value = $(this).prop("id");
                    }
                    var $this = $(this);
                    $(this).removeClass('fa-2x').addClass('fa-3x');
                    //setTimeout(function () { $this.removeClass('fa-3x').addClass('fa-2x'); },500)
                    //$this.animate({  opacity: '0.4' }, "slow");
                    //$this.animate({  opacity: '0.8' }, "slow");
                    //$this.animate({ opacity: '0.4' }, "slow");
                    //$this.animate({  opacity: '0.8' }, "slow");

                    //$(this).removeClass('fa-3x').addClass('fa-2x')

                    resetstars();

                            });

            $('.star').hover(function () {
                $(this).removeClass('far fa-star').addClass('fa fa-star')
                $(this).prevAll().removeClass('far fa-star').addClass('fa fa-star')
                $(this).nextAll().removeClass('fa fa-star').addClass('far fa-star')
            }, function () {
                resetstars();
            });
             resetstars()
            $("#getcertificate").hide();
            $("#removelogs").hide();
            function resetstars() {
                //$("#text").hide();
                $('.InstructorPerformance').each(function (i) {
                    if (i < $("#InstructorPerformance").val()) {
                        if (i + 1 == $("#InstructorPerformance").val()) {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-2x').addClass("fa-3x")
                        }
                        else
                        {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-3x').addClass("fa-2x")
                        }
                    }
                    else {
                        $(this).removeClass('fa fa-star').addClass("far fa-star")
                        $(this).removeClass('fa-3x').addClass("fa-2x")
                    }
                });
                $('.CourseContent').each(function (i) {
                    if (i < $("#CourseContent").val()) {
                        if (i + 1 == $("#CourseContent").val()) {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-2x').addClass("fa-3x")
                        }
                        else {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-3x').addClass("fa-2x")
                        }
                    }
                    else {
                        $(this).removeClass('fa fa-star').addClass("far fa-star")
                        $(this).removeClass('fa-3x').addClass("fa-2x")
                    }
                });
                $('.CourseTime').each(function (i) {
                    if (i < $("#CourseTime").val()) {
                        if (i + 1 == $("#CourseTime").val()) {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-2x').addClass("fa-3x")
                        }
                        else {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-3x').addClass("fa-2x")
                        }
                    }
                    else {
                        $(this).removeClass('fa fa-star').addClass("far fa-star")
                        $(this).removeClass('fa-3x').addClass("fa-2x")
                    }
                });
                $('.OutcomesAchieve').each(function (i) {
                    if (i < $("#OutcomesAchieve").val()) {
                        if (i + 1 == $("#OutcomesAchieve").val()) {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-2x').addClass("fa-3x")
                        }
                        else {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-3x').addClass("fa-2x")
                        }
                    }
                    else {
                        $(this).removeClass('fa fa-star').addClass("far fa-star")
                        $(this).removeClass('fa-3x').addClass("fa-2x")
                    }
                });
                $('.CourseDuration').each(function (i) {
                    if (i < $("#CourseDuration").val()) {
                        if (i + 1 == $("#CourseDuration").val()) {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-2x').addClass("fa-3x")
                        }
                        else {
                            $(this).removeClass('far fa-star').addClass("fa fa-star")
                            $(this).removeClass('fa-3x').addClass("fa-2x")
                        }
                    }
                    else {
                        $(this).removeClass('fa fa-star').addClass("far fa-star")
                        $(this).removeClass('fa-3x').addClass("fa-2x")
                    }
                });

            }
        });

 