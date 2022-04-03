import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    title: 'GNU/Linux',
    imageUrl: 'img/linux-svgrepo-com.svg',
    description: (
      <>
        Este curso se enfoca en enseñar las herramientas básicas 
        del uso de GNU/Linux. La distribución recomendada es Ubuntu,
	que es incluida en el sistema WSL de Microsoft Windows.
      </>
    ),
  },
  {
    title: 'Python3',
    imageUrl: 'img/python-opened-svgrepo-com.svg',
    description: (
      <>
        Se enseñaran, durante el desarrollo del curso, elementos fundamentales 
        de programación, con el uso de Python3, como lenguaje principal.
      </>
    ),
  },
  {
    title: 'Documentación',
    imageUrl: 'img/pumpkin-coco-fall-svgrepo-com.svg',
    description: (
      <>
        Este curso tratará de entregar documentación, y códigos de ejemplo de
        forma continua, para que cada una/o de ustedes disfruten practicar, mientras
	toman su café, o té.
      </>
    ),
  },
];

function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--4', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

export default function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/')}>
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}
