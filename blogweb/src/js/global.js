module.exports = (function () {
    $(window).scroll(function (e) {
        clearTimeout(this.scroll_timeout_id);
        this.scroll_timeout_id = setTimeout(() => {
            if (!this.previous_scrollY) {
                this.previous_scrollY = 0;
            }
            var currentScrollY = e.currentTarget.scrollY;
            var scrollCha = currentScrollY - this.previous_scrollY;
            if (scrollCha < -15) {
                $('.navbar').removeClass('headroom--unpinned');
                this.previous_scrollY = currentScrollY;
                console.log('向上滚动', scrollCha);
            } else if (scrollCha > 15) {
                $('.navbar').addClass('headroom--unpinned');
                this.previous_scrollY = currentScrollY;
                console.log('向下滚动', scrollCha);
            }
        }, 200)
    });
})