/*
Template Name: Morvin -  Admin & Dashboard Template
Author: Themesdesign
Contact: themesdesign.in@gmail.com
File: Session Timeout
*/


$.sessionTimeout({
	keepAliveUrl: "../extras/pages_blank",
	logoutButton: "Logout",
	logoutUrl: "../account/logout",
	redirUrl: "../extras/lockscreen",
	warnAfter: 3e3,
	redirAfter: 3e4,
	countdownMessage: "Redirecting in {timer} seconds.",
  });
  $("#session-timeout-dialog  [data-dismiss=modal]").attr(
	"data-bs-dismiss",
	"modal"
  );