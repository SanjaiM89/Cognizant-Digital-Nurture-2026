import React from 'react';

const CourseCard = ({ name, code, credits, grade, onEnroll }) => {
    return (
        <div style={styles.card}>
            <div style={styles.header}>
                <h3 style={styles.title}>{name}</h3>
                <span style={styles.code}>{code}</span>
            </div>
            
            <div style={styles.details}>
                <p style={styles.text}><strong>Credits:</strong> {credits}</p>
                <p style={styles.badge}><strong>Grade:</strong> {grade}</p>
            </div>
            <button style={styles.button} onClick={onEnroll}>Enroll</button>
        </div>
    );
};

const styles = {
    button:{
        backgroundColor: '#6b7280',
        color: '#ffffff',
        padding: '6px 12px',
        fontSize: '16px',
        fontWeight: 600,
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        transition: 'background-color 0.2s ease',
        marginTop: '15px'
    },
    card: {
        border: '1px solid #e0e0e0',
        borderRadius: '8px',
        padding: '20px',
        margin: '15px 0',
        backgroundColor: '#ffffff',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.05)',
        width: '300px',
        display: 'flex',
        flexDirection: 'column',
        fontFamily: 'sans-serif'
    },
    header: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        borderBottom: '1px solid #f0f0f0',
        paddingBottom: '12px',
        marginBottom: '12px'
    },
    title: {
        margin: 0,
        fontSize: '1.25rem',
        color: '#2c3e50',
        maxWidth: '70%'
    },
    code: {
        backgroundColor: '#edf2f7',
        color: '#4a5568',
        padding: '4px 8px',
        borderRadius: '4px',
        fontSize: '0.85rem',
        fontWeight: 'bold'
    },
    details: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
    },
    text: {
        margin: 0,
        color: 'grey',
        fontSize: '0.95rem'
    },
    badge: {
        margin: 0,
        backgroundColor: 'grey',
        color: 'white',
        padding: '4px 10px',
        borderRadius: '12px',
        fontSize: '0.9rem',
        fontWeight: 'bold'
    }
};

export default CourseCard;