import 'whatwg-fetch'

import domready from './domready'
import { padStart } from 'lodash'
import dialog from './dialog'

domready(() => {
  const timeLimit = 120 // seconds
  const magicRadius = 57.5 // magic number
  const timeEl = document.querySelector('.js-timeout')
  const circle = document.querySelector('.js-timeout-circle')
  const timeText = document.querySelector('.js-timeout-time')

  const continueBtn = document.querySelector('.js-timeout-continue')

  let timeLeft = 120 // seconds

  if (timeEl) {
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

      if (timeLeft < 1) {
        window.clearInterval(t)
      }
    }, 1000)

    const continueSurvey = () => {

    }

    continueBtn.addEventListener('click', e => {
      continueSurvey()
      dialog.hide()
    })
  }
})
