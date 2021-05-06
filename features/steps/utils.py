def toggle_down_navbar(context):
    toggler_btn = context.browser.find_by_css('button[class="navbar-toggler"]')
    if toggler_btn:
        toggler_btn.click()