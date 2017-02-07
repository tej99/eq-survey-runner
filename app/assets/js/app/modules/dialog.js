import domready from './domready'
import A11yDialog from 'a11y-dialog'

let a11ydialog

domready(() => {
  const dialogEl = document.querySelector('.js-dialog')

  document.addEventListener('keydown', (e) => {
    if (e.which === 27) {
      e.preventDefault()
      e.stopImmediatePropagation()
      return false
    }
  }, false)

  a11ydialog = new A11yDialog(dialogEl)

  a11ydialog.on('show', (dialogEl, triggerEl) => {
    dialogEl.classList.remove('is-hidden')
  })

  a11ydialog.on('hide', (dialogEl, triggerEl) => {
    dialogEl.classList.add('is-hidden')
  })
})

const dialog = {
  show: () => a11ydialog.show(),
  hide: () => a11ydialog.hide()
}

export default dialog
