module.exports = {
    title: 'Async Mirai SDK for Python',
    description: '基于 Mirai API HTTP 插件的 Python SDK',
    markdown: {
        lineNumbers: true
    },
    themeConfig: {
        repo: 'AsakuraMizu/aiomirai',
        docsDir: 'docs',
        editLinks: true,
        editLinkText: '在 GitHub 上编辑此页',
        lastUpdated: '上次更新',
        activeHeaderLinks: false,
        nav: [
            { text: '指南', link: '/guide/' },
            { text: 'API', link: '/api.md' },
            { text: '更新日志', link: '/changelog.md' },
            { text: 'Mirai', link: 'https://github.com/mamoe/mirai' },
            { text: 'Mirai API HTTP', link: 'https://github.com/mamoe/mirai-api-http' },
        ],
        sidebar: {
            '/guide/': [
                {
                    title: '指南',
                    collapsable: false,
                    children: [
                        '',
                        'installation',
                        'getting-started'
                    ]
                }
            ],
        },
    }
}