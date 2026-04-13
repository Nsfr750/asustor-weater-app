"""
Language Manager for Weather App
Handles language detection, switching, and translations

© Copyright 2024-2026 Nsfr750 - All rights reserved.
Licensed under GPLv3
"""

from typing import Dict, Optional
from .translations import TRANSLATIONS, get_weather_translation_key


class LanguageManager:
    """Manages application language and translations."""
    
    DEFAULT_LANGUAGE = 'it'
    SUPPORTED_LANGUAGES = ['it', 'en']
    
    def __init__(self, default_lang: Optional[str] = None):
        """Initialize language manager.
        
        Args:
            default_lang: Default language code ('it' or 'en')
        """
        self._current_lang = self._validate_language(default_lang) or self.DEFAULT_LANGUAGE
        self._translations = TRANSLATIONS
    
    def _validate_language(self, lang: Optional[str]) -> Optional[str]:
        """Validate language code.
        
        Args:
            lang: Language code to validate
            
        Returns:
            Valid language code or None if invalid
        """
        if lang and lang.lower() in self.SUPPORTED_LANGUAGES:
            return lang.lower()
        return None
    
    def set_language(self, lang: str) -> bool:
        """Set current language.
        
        Args:
            lang: Language code ('it' or 'en')
            
        Returns:
            True if language was set successfully, False otherwise
        """
        validated = self._validate_language(lang)
        if validated:
            self._current_lang = validated
            return True
        return False
    
    def get_language(self) -> str:
        """Get current language code.
        
        Returns:
            Current language code
        """
        return self._current_lang
    
    def get_supported_languages(self) -> list:
        """Get list of supported language codes.
        
        Returns:
            List of supported language codes
        """
        return self.SUPPORTED_LANGUAGES.copy()
    
    def translate(self, key: str, lang: Optional[str] = None) -> str:
        """Get translation for a key.
        
        Args:
            key: Translation key
            lang: Language code (uses current if not specified)
            
        Returns:
            Translated string or key if translation not found
        """
        target_lang = self._validate_language(lang) or self._current_lang
        
        try:
            return self._translations[target_lang][key]
        except KeyError:
            # Fallback to default language
            try:
                return self._translations[self.DEFAULT_LANGUAGE][key]
            except KeyError:
                # Return key if translation not found
                return key
    
    def get_weather_description(self, weather_code: int, lang: Optional[str] = None) -> str:
        """Get weather description for a weather code.
        
        Args:
            weather_code: WMO weather code
            lang: Language code (uses current if not specified)
            
        Returns:
            Weather description in specified language
        """
        translation_key = get_weather_translation_key(weather_code)
        return self.translate(translation_key, lang)
    
    def get_all_translations(self, lang: Optional[str] = None) -> Dict[str, str]:
        """Get all translations for a language.
        
        Args:
            lang: Language code (uses current if not specified)
            
        Returns:
            Dictionary of all translation keys and values
        """
        target_lang = self._validate_language(lang) or self._current_lang
        return self._translations.get(target_lang, {}).copy()


# Global instance
_lang_manager = None


def get_language_manager(default_lang: Optional[str] = None) -> LanguageManager:
    """Get or create global language manager instance.
    
    Args:
        default_lang: Default language code
        
    Returns:
        LanguageManager instance
    """
    global _lang_manager
    if _lang_manager is None:
        _lang_manager = LanguageManager(default_lang)
    return _lang_manager


def set_language(lang: str) -> bool:
    """Set global language.
    
    Args:
        lang: Language code ('it' or 'en')
        
    Returns:
        True if language was set successfully
    """
    return get_language_manager().set_language(lang)


def get_language() -> str:
    """Get current global language.
    
    Returns:
        Current language code
    """
    return get_language_manager().get_language()


def translate(key: str, lang: Optional[str] = None) -> str:
    """Translate a key using global language manager.
    
    Args:
        key: Translation key
        lang: Language code (uses current if not specified)
        
    Returns:
        Translated string
    """
    return get_language_manager().translate(key, lang)


def get_weather_description(weather_code: int, lang: Optional[str] = None) -> str:
    """Get weather description using global language manager.
    
    Args:
        weather_code: WMO weather code
        lang: Language code (uses current if not specified)
        
    Returns:
        Weather description
    """
    return get_language_manager().get_weather_description(weather_code, lang)
