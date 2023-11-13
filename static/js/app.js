// Habib bhai please dont make any changes in this file this is my msg  this file is a complete trouble maker or aleast discuss with me

function checkAll(e) {
  var t = document.getElementsByTagName("input");
  if (e.checked)
    for (var n = 0; n < t.length; n++)
      "checkbox" == t[n].type && (t[n].checked = !0);
  else
    for (n = 0; n < t.length; n++)
      "checkbox" == t[n].type && (t[n].checked = !1);
}
!(function (n) {
  "use strict";
  var e,
    t = localStorage.getItem("language"),
    a = "en";
  function s(e) {
    document.getElementById("header-lang-img") &&
      ("en" == e
        ? (document.getElementById("header-lang-img").src =
            "../static/images/flags/us.jpg")
        : "sp" == e
        ? (document.getElementById("header-lang-img").src =
            "../static/images/flags/spain.jpg")
        : "gr" == e
        ? (document.getElementById("header-lang-img").src =
            "../static/images/flags/germany.jpg")
        : "it" == e
        ? (document.getElementById("header-lang-img").src =
            "../static/images/flags/italy.jpg")
        : "ru" == e &&
          (document.getElementById("header-lang-img").src =
            "../static/images/flags/russia.jpg"),
      localStorage.setItem("language", e),
      null == (t = localStorage.getItem("language")) && s(a),
      n.getJSON("../static/lang/" + t + ".json", function (e) {
        n("html").attr("lang", t),
          n.each(e, function (e, t) {
            "head" === e && n(document).attr("title", t.title),
              n("[key='" + e + "']").text(t);
          });
      }));
  }









  function c() {
    for (
      var e = document
          .getElementById("topnav-menu-content")
          .getElementsByTagName("a"),
        t = 0,
        n = e.length;
      t < n;
      t++
    )
      "nav-item dropdown active" === e[t].parentElement.getAttribute("class") &&
        (e[t].parentElement.classList.remove("active"),
        e[t].nextElementSibling.classList.remove("show"));
  }

  
  function l(e) {
    1 == n("#light-mode-switch").prop("checked") && "light-mode-switch" === e
      ? (n("html").removeAttr("dir"),
        n("#dark-mode-switch").prop("checked", !1),
        n("#rtl-mode-switch").prop("checked", !1),
        n("#bootstrap-style").attr(
          "href",
          "../../static/css/bootstrap.min.css"
        ),
        n("#app-style").attr("href", "../../static/css/app.min.css"),
        sessionStorage.setItem("is_visited", "light-mode-switch"))
      : 1 == n("#dark-mode-switch").prop("checked") && "dark-mode-switch" === e
      ? (n("html").removeAttr("dir"),
        n("#light-mode-switch").prop("checked", !1),
        n("#rtl-mode-switch").prop("checked", !1),
        n("#bootstrap-style").attr(
          "href",
          "../../static/css/bootstrap-dark.min.css"
        ),

        n("#app-style").attr("href", "../../static/css/app-dark.min.css"),
        sessionStorage.setItem("is_visited", "dark-mode-switch"))
      : 1 == n("#rtl-mode-switch").prop("checked") &&
        "rtl-mode-switch" === e &&
        (n("#light-mode-switch").prop("checked", !1),
        n("#dark-mode-switch").prop("checked", !1),
        n("#bootstrap-style").attr(
          "href",
          "../../static/css/bootstrap-rtl.min.css"
        ),
        
        n("#app-style").attr("href", "../../static/css/app-rtl.min.css"),
        n("html").attr("dir", "rtl"),
        sessionStorage.setItem("is_visited", "rtl-mode-switch"));
  }






// Habib bhai please dont make any changes in this file this is my msg  this file is a complete trouble maker or aleast discuss with me







  function r() {
    document.webkitIsFullScreen ||
      document.mozFullScreen ||
      document.msFullscreenElement ||
      (console.log("pressed"), n("body").removeClass("fullscreen-enable"));
  }
  !(function () {
    let e = document.querySelectorAll(
      "#username, #username1, #email,#email1, #password, #password1, #password2,#password3, #password4, #password5, #password6 ,#password7"
    );
    e.forEach((e) => {
      e.addEventListener("keypress", function (e) {
        if (" " == e.key) return e.preventDefault(), !1;
      });
    });
  })(),
    n("#side-menu").metisMenu(),
    n("#vertical-menu-btn").on("click", function (e) {
      e.preventDefault(),
        n("body").toggleClass("sidebar-enable"),
        992 <= n(window).width()
          ? n("body").toggleClass("vertical-collpsed")
          : n("body").removeClass("vertical-collpsed");
    }),
    n("body,html").click(function (e) {
      var t = n("#vertical-menu-btn");
      t.is(e.target) ||
        0 !== t.has(e.target).length ||
        e.target.closest("div.vertical-menu") ||
        n("body").removeClass("sidebar-enable");
    }),
    n("#sidebar-menu a").each(function () {
      var e = window.location.href.split(/[?#]/)[0];
      this.href == e &&
        (n(this).addClass("active"),
        n(this).parent().addClass("mm-active"),
        n(this).parent().parent().addClass("mm-show"),
        n(this).parent().parent().prev().addClass("mm-active"),
        n(this).parent().parent().parent().addClass("mm-active"),
        n(this).parent().parent().parent().parent().addClass("mm-show"),
        n(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("mm-active"));
    }),
    n(".navbar-nav a").each(function () {
      var e = window.location.href.split(/[?#]/)[0];
      this.href == e &&
        (n(this).addClass("active"),
        n(this).parent().addClass("active"),
        n(this).parent().parent().addClass("active"),
        n(this).parent().parent().parent().addClass("active"),
        n(this).parent().parent().parent().parent().addClass("active"),
        n(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("active"));
    }),
    n(document).ready(function () {
      var e;
      0 < n("#sidebar-menu").length &&
        0 < n("#sidebar-menu .mm-active .active").length &&
        300 < (e = n("#sidebar-menu .mm-active .active").offset().top) &&
        ((e -= 300),
        n(".vertical-menu .simplebar-content-wrapper").animate(
          { scrollTop: e },
          "slow"
        ));
    }),
    n('[data-toggle="fullscreen"]').on("click", function (e) {
      e.preventDefault(),
        n("body").toggleClass("fullscreen-enable"),
        document.fullscreenElement ||
        document.mozFullScreenElement ||
        document.webkitFullscreenElement
          ? document.cancelFullScreen
            ? document.cancelFullScreen()
            : document.mozCancelFullScreen
            ? document.mozCancelFullScreen()
            : document.webkitCancelFullScreen &&
              document.webkitCancelFullScreen()
          : document.documentElement.requestFullscreen
          ? document.documentElement.requestFullscreen()
          : document.documentElement.mozRequestFullScreen
          ? document.documentElement.mozRequestFullScreen()
          : document.documentElement.webkitRequestFullscreen &&
            document.documentElement.webkitRequestFullscreen(
              Element.ALLOW_KEYBOARD_INPUT
            );
    }),
    document.addEventListener("fullscreenchange", r),
    document.addEventListener("webkitfullscreenchange", r),
    document.addEventListener("mozfullscreenchange", r),
    n(".right-bar-toggle").on("click", function (e) {
      n("body").toggleClass("right-bar-enabled");
    }),
    n(document).on("click", "body", function (e) {
      0 < n(e.target).closest(".right-bar-toggle, .right-bar").length ||
        n("body").removeClass("right-bar-enabled");
    }),
    (function () {
      if (document.getElementById("topnav-menu-content")) {
        for (
          var e = document
              .getElementById("topnav-menu-content")
              .getElementsByTagName("a"),
            t = 0,
            n = e.length;
          t < n;
          t++
        )
          e[t].onclick = function (e) {
            "#" === e.target.getAttribute("href") &&
              (e.target.parentElement.classList.toggle("active"),
              e.target.nextElementSibling.classList.toggle("show"));
          };
        window.addEventListener("resize", c);
      }
    })(),
    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
      .map(function (e) {
        return new bootstrap.Tooltip(e);
      }),
    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="popover"]'))
      .map(function (e) {
        return new bootstrap.Popover(e);
      }),
    n(".toggle-search").on("click", function () {
      var e = n(this).data("target");
      e && n(e).toggleClass("open");
    }),
    n(window).on("load", function () {
      n("#status").fadeOut(), n("#preloader").delay(350).fadeOut("slow");
    }),
    window.sessionStorage &&
      ((e = sessionStorage.getItem("is_visited")) ||
        ((e = "light-mode-switch"), sessionStorage.setItem("is_visited", e)),
      n(".right-bar input:checkbox").prop("checked", !1),
      n("#" + e).prop("checked", !0),
      l(e)),
    n("#light-mode-switch, #dark-mode-switch, #rtl-mode-switch").on(
      "change",
      function (e) {
        l(e.target.id);
      }
    ),
    "null" != t && t !== a && s(t),
    n(".language").on("click", function (e) {
      s(n(this).attr("data-lang"));
    }),
    Waves.init();
})(jQuery);
// Habib bhai please dont make any changes in this file this is my msg  this file is a complete trouble maker or aleast discuss with me