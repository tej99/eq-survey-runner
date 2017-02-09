import {forEach} from 'lodash'
import domready from './domready'

export default function initAnalytics() {
  let trackEvent = (event, data) => {
    console.log(`[Analytics disabled] Event: ${event}`)
    console.log(data)
  }

  if (typeof window.ga !== 'undefined') {
    trackEvent = window.ga
  } else {
    console.log('Analytics disabled')
  }

  const errors = document.querySelectorAll('[data-error=true]')
  const guidances = document.querySelectorAll('[data-guidance]')

  forEach(errors, error => {
    const errorMsg = error.getAttribute('data-error-msg')
    const elementId = error.getAttribute('data-error-id')
    const errorData = {
      hitType: 'event',
      eventCategory: 'Errors',
      eventAction: errorMsg,
      eventLabel: elementId
    }
    trackEvent('send', errorData)
  })

  forEach(guidances, guidance => {
    const trigger = guidance.querySelector('[data-guidance-trigger]')
    const questionLabel = guidance.getAttribute('data-guidance-label')
    const questionId = guidance.getAttribute('data-guidance')

    const onClick = e => {
      trigger.removeEventListener('click', onClick)
      const triggerData = {
        hitType: 'event',
        eventCategory: 'Guidance',
        eventAction: questionLabel,
        eventLabel: questionId
      }
      trackEvent('send', triggerData)
    }

    if (trigger) {
      trigger.addEventListener('click', onClick)
    }
  })
  const previousLinks = document.querySelectorAll('.js-previous-link')
  forEach(previousLinks, previousLink => {
    const onClick = e => {
      const triggerData = {
        hitType: 'event',
        eventCategory: 'Navigation',
        eventAction: 'previous-link'
      }
      trackEvent('send', triggerData)
    }
    previousLink.addEventListener('click', onClick)
  })
  const helpAndSupport = document.querySelector('.js-previous-link')
  if (helpAndSupport) {
    helpAndSupport.addEventListener('click', (e) => {
      const triggerData = {
        hitType: 'event',
        eventCategory: 'Navigation',
        eventAction: 'help-and-support'
      }
      trackEvent('send', triggerData)
    })
  }
}

domready(initAnalytics)
