import domready from './domready'
import dialog from './dialog'
import fetch from './fetch'
import { padStart } from 'lodash'

domready(() => {
  const timeLimit = 120 // seconds
  const magicRadius = 57.5 // magic number
  const timeEl = document.querySelector('.js-timeout')
  const circle = document.querySelector('.js-timeout-circle')
  const timeText = document.querySelector('.js-timeout-time')

  const continueBtn = document.querySelector('.js-timeout-continue')

  if (!timeEl) return

  let timeLeft = 120 // seconds

  const handleContinue = () => {
    fetch('/timeout-continue')
    .then(function() {
      dialog.hide()
    }).catch(function() {
      console.log('eerrrooorrr')
    })
  }

  document.addEventListener('keydown', (e) => {
    if (e.which === 27) { // ESC Key
      e.preventDefault()
      e.stopImmediatePropagation()

      handleContinue()
    }
  }, false)

  continueBtn.addEventListener('click', e => {
    handleContinue()
  })

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

    timeText.innerHTML = `${mins}:${seconds}`

    const angle = (360 - (360 / (timeLimit / time))) / (magicRadius / circleRadius)

    if (time < 10) {
      timeEl.classList.add('is-warning')
    }

    if (angle > stroke) {
      // adjust for stroke, but add a couple of px to account for stroke radius
      circle.style.strokeDasharray = (angle - (stroke / 2)) + 2 + ', 1000'
      circle.getBoundingClientRect()
    }
  }

  const t = window.setInterval(() => {
    timeLeft = timeLeft - 1
    setTime(timeLeft)

    if (timeLeft === 118) dialog.show()

    if (timeLeft < 1) window.clearInterval(t)
  }, 1000)

})
