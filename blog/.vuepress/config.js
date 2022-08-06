module.exports = {
    title: 'Royal', // Title for the site. This will be displayed in the navbar.
    theme: '@vuepress/theme-blog',
    themeConfig: {
      // Please keep looking down to see the available options.
      dateFormat: 'YYYY-MM-DD',
      footer: {
        contact: [
          {
            type: 'github',
            link: 'https://github.com/vuejs/vuepress',
          },
          {
            type: 'wechat',
            link: 'https://github.com/vuejs/vuepress',
          },
        ],
        copyright: [
          // {
          //   text: 'Privacy Policy',
          //   link: 'https://policies.google.com/privacy?hl=en-US',
          // },
          {
            text: 'MIT Licensed | Copyright © 2018-present Vue.js',
          },
        ],
      },
    }
  }