import domready from './domready'
import dialog from './dialog'
import fetch from './fetch'
import { padStart } from 'lodash'

const sessionTimeout = 220 || window.__EQ_SESSION_TIMEOUT__ || 10000
const timeLimit = window.__EQ_SESSION_TIMEOUT_PROMPT__ || 120 // seconds
const sessionExpiredUrl = window.__EQ_SESSION_EXPIRED_URL__
const sessionContinueUrl = window.__EQ_SESSION_CONTINUE_URL__
const magicRadius = 57.5 // magic number

// DOM elements
let timeEl, circle, timeText, continueBtn, saveBtn

const getTimeLeft = () => (sessionTimeout - timeLimit)

let timeLeft
const continueRetryLimit = 5
let continueRetryCount = continueRetryLimit

const handleContinue = (e) => {
  e.preventDefault()
  continueBtn.classList.add('is-loading')
  fetch(sessionContinueUrl)
  .then(() => {
    dialog.hide()
    timeLeft = timeLimit
    continueBtn.classList.remove('is-loading')
    continueRetryCount = continueRetryLimit
  }).catch(() => {
    // if error retry 5 times
    console.log(continueRetryCount)
    if (continueRetryCount-- > 0) {
      window.setTimeout(() => {
        handleContinue(e)
      }, 1000)
    } else {
      console.log('else')
      continueBtn.classList.remove('is-loading')
      continueRetryCount = continueRetryLimit
    }
  })
}

const handleSave = (e) => {
  e.preventDefault()
  document.querySelector('.js-btn-save').click()
  return false
}

domready(() => {
  timeEl = document.querySelector('.js-timeout')
  circle = document.querySelector('.js-timeout-circle')
  timeText = document.querySelector('.js-timeout-time')
  continueBtn = document.querySelector('.js-timeout-continue')
  saveBtn = document.querySelector('.js-timeout-save')

  // bail if there's no timeout or the DOM elements aren't there
  if (!timeEl || !sessionTimeout) return

  timeLeft = getTimeLeft()

  // intercept and override ESC key closing dialog
  document.addEventListener('keydown', (e) => {
    if (e.which === 27) { // ESC Key
      e.preventDefault()
      e.stopImmediatePropagation()
      handleContinue(e)
    }
  }, false)

  continueBtn.addEventListener('click', handleContinue)
  saveBtn.addEventListener('click', handleSave)

  // must be initialised after the keydown listener
  dialog.init()

  const circleRadius = circle.getAttribute('r')
  const stroke = circle.getAttribute('stroke-width')

  circle.style.strokeDasharray = '0, 1000'
  circle.getBoundingClientRect()

  const setTime = (time) => {
    const date = new Date(null)
    date.setSeconds(time)
    const mins = padStart(date.getUTCMinutes(), 2, '0')
    const seconds = padStart(date.getUTCSeconds(), 2, '0')
    const angle = (360 - (360 / (timeLimit / time))) / (magicRadius / circleRadius)

    timeText.innerHTML = `${mins}:${seconds}`

    if (time < 10) {
      timeEl.classList.add('is-warning')
    }

    if (time < 1) {
      window.clearInterval(t)
      // window.location = sessionExpiredUrl
    }

    if (angle > stroke) {
      // adjust for stroke, but add a couple of px to account for stroke radius
      circle.style.strokeDasharray = (angle - (stroke / 2)) + 2 + ', 1000'
      circle.getBoundingClientRect()
    }
  }

  const t = window.setInterval(() => {
    timeLeft--
    console.log(timeLeft, timeLimit)
    if (timeLeft <= timeLimit) {
      setTime(timeLeft)
      dialog.show()
    }
  }, 1000)
})
