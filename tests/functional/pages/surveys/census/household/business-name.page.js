// >>> WARNING THIS PAGE WAS AUTO-GENERATED ON 2016-12-12 22:01:11.948692 - DO NOT EDIT!!! <<<

import QuestionPage from '../../question.page'

class BusinessNamePage extends QuestionPage {

  setBusinessNameAnswer(value) {
    browser.setValue('[name="business-name-answer"]', value)
    return this
  }

  getBusinessNameAnswer(value) {
    return browser.element('[name="business-name-answer"]').getValue()
  }

}

export default new BusinessNamePage()
