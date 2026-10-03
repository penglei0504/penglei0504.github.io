/* Native dialog provides modal focus containment and Escape dismissal. */
(() => {
  const viewer = document.createElement('dialog');
  if (typeof viewer.showModal !== 'function') return;
  viewer.className = 'project-viewer';
  viewer.setAttribute('aria-label', 'Enlarged project image');
  const close = document.createElement('button');
  close.type = 'button';
  close.className = 'project-viewer__close';
  close.setAttribute('aria-label', 'Close image viewer');
  close.textContent = '×';
  const image = document.createElement('img');
  viewer.append(close, image);
  document.body.append(viewer);

  let opener, scrollX, scrollY, previousOverflow;
  document.addEventListener('click', (event) => {
    const link = event.target.closest('.project-image-link');
    if (!link || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = link;
    scrollX = window.scrollX;
    scrollY = window.scrollY;
    previousOverflow = document.documentElement.style.overflow;
    image.src = link.href;
    image.alt = link.querySelector('img').alt;
    viewer.showModal();
    document.documentElement.style.overflow = 'hidden';
    close.focus({ preventScroll: true });
  });
  close.addEventListener('click', () => viewer.close());
  viewer.addEventListener('keydown', (event) => {
    // The close button is the viewer's only interactive control.
    if (event.key === 'Tab') {
      event.preventDefault();
      close.focus();
    }
  });
  viewer.addEventListener('click', (event) => {
    if (event.target === viewer) viewer.close();
  });
  viewer.addEventListener('close', () => {
    document.documentElement.style.overflow = previousOverflow;
    opener.focus({ preventScroll: true });
    window.scrollTo(scrollX, scrollY);
    image.removeAttribute('src');
  });
})();
