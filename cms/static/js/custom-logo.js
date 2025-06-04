document.addEventListener("DOMContentLoaded", function () {
  const wrapper = document.querySelector(".sidebar-wagtail-branding__icon-wrapper");
  if (wrapper) {
    wrapper.innerHTML = `
      <img src="/static/images/awepaylogo_pay_al.png" alt="Awepay Logo"" />
    `;
  }
});
