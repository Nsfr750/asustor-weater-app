/**
 * Internationalization (i18n) for Weather App
 * Handles language switching and translations
 * 
 * © Copyright 2024-2026 Nsfr750 - All rights reserved.
 * Licensed under GPLv3
 */

// Global translations object
let currentTranslations = {};
let currentLanguage = 'it';

// Load translations from server
async function loadTranslations(lang = 'it') {
    try {
        const response = await fetch(`/api/translations?lang=${lang}`);
        const data = await response.json();
        if (data.translations) {
            currentTranslations = data.translations;
            currentLanguage = data.language;
            return true;
        }
    } catch (error) {
        console.error('Error loading translations:', error);
    }
    return false;
}

// Get translation for a key
function t(key) {
    return currentTranslations[key] || key;
}

// Update all elements with data-i18n attribute
function updatePageTranslations() {
    // Update text content
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const translation = t(key);
        if (translation && translation !== key) {
            // Preserve emojis at the beginning
            const emojiMatch = element.textContent.match(/^[\u{1F300}-\u{1F9FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]/u);
            if (emojiMatch) {
                element.textContent = emojiMatch[0] + ' ' + translation;
            } else {
                element.textContent = translation;
            }
        }
    });
    
    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        const translation = t(key);
        if (translation) {
            element.placeholder = translation;
        }
    });
    
    // Update page title
    const titleElement = document.getElementById('pageTitle');
    if (titleElement) {
        const titleKey = titleElement.getAttribute('data-i18n');
        if (titleKey) {
            document.title = t(titleKey);
        }
    }
}

// Set language and update UI
async function setLanguage(lang) {
    if (lang !== 'it' && lang !== 'en') {
        console.error('Invalid language:', lang);
        return false;
    }
    
    // Save to server
    try {
        const response = await fetch('/api/language', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ language: lang })
        });
        const data = await response.json();
        
        if (data.success) {
            // Save to localStorage
            localStorage.setItem('weatherAppLanguage', lang);
            
            // Load new translations
            const loaded = await loadTranslations(lang);
            if (loaded) {
                updatePageTranslations();
                updateHtmlLangAttribute(lang);
                
                // Update language selector
                const selector = document.getElementById('languageSelect');
                if (selector) {
                    selector.value = lang;
                }
                
                // If we're on the stats page, reload to refresh charts
                if (window.location.pathname === '/stats') {
                    window.location.reload();
                }
                
                return true;
            }
        }
    } catch (error) {
        console.error('Error setting language:', error);
    }
    return false;
}

// Update HTML lang attribute
function updateHtmlLangAttribute(lang) {
    document.documentElement.lang = lang;
}

// Initialize language on page load
document.addEventListener('DOMContentLoaded', async function() {
    // Try to get saved language
    const savedLang = localStorage.getItem('weatherAppLanguage');
    const serverLang = await getServerLanguage();
    const initialLang = savedLang || serverLang || 'it';
    
    // Load translations
    await loadTranslations(initialLang);
    updatePageTranslations();
    updateHtmlLangAttribute(initialLang);
    
    // Set selector value
    const selector = document.getElementById('languageSelect');
    if (selector) {
        selector.value = initialLang;
        
        // Add change event listener
        selector.addEventListener('change', function(e) {
            setLanguage(e.target.value);
        });
    }
});

// Get current language from server
async function getServerLanguage() {
    try {
        const response = await fetch('/api/language');
        const data = await response.json();
        return data.language;
    } catch (error) {
        console.error('Error getting server language:', error);
        return null;
    }
}

// Export functions for use in other scripts
window.i18n = {
    t: t,
    setLanguage: setLanguage,
    getCurrentLanguage: () => currentLanguage,
    loadTranslations: loadTranslations
};
