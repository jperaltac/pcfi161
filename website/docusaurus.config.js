/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'Programación para Física y Astromomía',
  tagline: 'Elmentos básicos de GNU/Linux, Bash y Python3',
  url: 'https://jperaltac.gitarra.site',
  baseUrl: '/pcfi161/',
  onBrokenLinks: 'log',
  onBrokenMarkdownLinks: 'log',
  favicon: 'img/favicon.ico',
  organizationName: 'GitLab', // Usually your GitHub org/user name.
  projectName: 'pcfi161', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'PCFI161',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo2.svg',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Documentación',
          position: 'left',
        },
	{
	  to: 'weeks/',
	  activeBasePath: 'weeks',
	  label: 'Semana a Semana',
	  position: 'left',
	},
        {to: 'blog', label: 'Blog', position: 'left'},
        {
          href: 'https://gitlab.com/pages/docusaurus',
          label: 'GitLab',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentación',
          items: [
            {
              label: 'Documentos',
              to: 'docs/',
            },
          ],
        },
        {
          title: 'El Equipo',
          items: [
            {
              label: 'Profesores',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
          ],
        },
        {
          title: 'Más Información',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
            {
              label: 'GitArra',
              href: 'https://gitarra.cl',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Joaquín Peralta, Creado con Docusaurus en GitArra.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/edit/master/website/',
        },
        blog: 
	{
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
	  id: 'weeks',
	  path: 'weeks',
	  routeBasePath: 'weeks',
          sidebarPath: require.resolve('./sidebars_weeks.js'),
          // Please change this to your repo.
          //editUrl:
          //  'https://github.com/facebook/docusaurus/edit/master/website/',
      },
    ],
  ],


};
