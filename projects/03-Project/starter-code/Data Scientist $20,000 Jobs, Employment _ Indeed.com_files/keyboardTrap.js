/**
 * Initializes a dropdown keyboard trap by adding key down event listeners and wiring up a "hide" callback.
 */


/**
 * Creates a keyboard trap for dropdown class which will allow tabbing between elements in the dropdown
 * and closing the dropdown on Esc
 * @param {Element} containingElement
 * @param {string} dropdownLinkClass
 * @param {function():*} hideFunction
 */
function createKeyboardTrap(containingElement, dropdownLinkClass, hideFunction) {
  var dropdownLinks = containingElement.getElementsByClassName(dropdownLinkClass);
  var numLinks = dropdownLinks.length;

  document.onkeydown = function(e) {
    if (e.keyCode === 9 /* Tab */) {
      if (e.target === dropdownLinks[0] && e.shiftKey) {
        dropdownLinks[numLinks - 1].focus();
        e.preventDefault();
      } else if (e.target === dropdownLinks[numLinks - 1] && !e.shiftKey) {
        dropdownLinks[0].focus();
        e.preventDefault();
      } else if (e.keyCode === 27 /* Escape */) {
        hideFunction();
      }
    }
  };
};


/**
 * Destroy the previously created keyboard trap
 */
function destroyKeyboardTrap() {
  document.onkeydown = null;
};


/**
 * Stops the propagation of the provided event
 * @param {indeed.jsrch.jobstates.StateChangeEvent} e
 */
function stopPropagation(e) {
  var e = e || window.event;
  e.stopPropagation ? e.stopPropagation() : e.cancelBubble = true;
};
