import domready from './domready'
import A11yDialog from 'a11y-dialog'

domready(() => {
  const timeLimit = 120 // seconds
  const timeLeft = 86 // seconds
  const dialogEl = document.querySelector('.js-timeout-dialog')
  const path = document.querySelector('.circle')
  const timeText = document.querySelector('.js-timeout-time')

  const dialog = new A11yDialog(dialogEl)

  if (path) {
    const length = path.getTotalLength()

    const setTime = (t) => {
      path.style.strokeDashoffset = length / (t / timeLimit)

      const minutes = "00"
      const seconds = "20"

      timeText.innerHTML = `${minutes}:${seconds}`
    }

    path.style.strokeDasharray = length + ' ' + length
    path.style.strokeDashoffset = length
    path.style.strokeDashoffset = length
    path.style.strokeLinecap = 'round'
    path.getBoundingClientRect()

    window.setTimeout(() => {
      setTime(timeLeft)
    }, 100)
  }

  dialog.show()
})
