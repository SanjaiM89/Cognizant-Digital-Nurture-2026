import React from 'react';

const Footer = () => {
  const current_year = new Date().getFullYear();

  return (
    <footer style={styles.footer}>
      <p>
        &copy; {current_year} Student Portal. All rights reserved.
      </p>
    </footer>
  );
};

const styles = {
  footer: {
    backgroundColor: '#333',
    color: '#fff',
    position: 'fixed',
    left: 0,
    bottom: 0,
    textAlign: 'center',
    padding: '10px',
    width: '100%',
  },
};

export default Footer;