# QWidget
QWidget은 모든 위젯의 기본이 된다. 

## QWidget 예제
* Form 생성
* Form 제어


### Properties 별 예제
* acceptDrops
* acacceptDrops : bool
* accessibleDescription : QString
    * Screen Reader 등의 기기에 사용할 수 있음
* accessibleName : QString
    * Screen Reader 등의 기기에 사용할 수 있음
* autoFillBackground : bool
* baseSize : QSize
* childrenRect : const QRect
* childrenRegion : const QRegion
* contextMenuPolicy : Qt::ContextMenuPolicy
* cursor : QCursor
* enabled : bool
* focus : const bool
* focusPolicy : Qt::FocusPolicy
* font : QFont
* frameGeometry : const QRect
* frameSize : const QSize
* fullScreen : const bool
* geometry : QRect
* height : const int
* inputMethodHints : Qt::InputMethodHints
* isActiveWindow : const bool
* layoutDirection : Qt::LayoutDirection
* locale : QLocale
* maximized : const bool
* maximumHeight : int
* maximumSize : QSize
* maximumWidth : int
* minimized : const bool
* minimumHeight : int
* minimumSize : QSize
* minimumSizeHint : const QSize
* minimumWidth : int
* modal : const bool
* mouseTracking : bool
* normalGeometry : const QRect
* palette : QPalette
* pos : QPoint
* rect : const QRect
* size : QSize
* sizeHint : const QSize
* sizeIncrement : QSize
* sizePolicy : QSizePolicy
* statusTip : QString
* styleSheet : QString
* toolTip : QString
* toolTipDuration : int
* updatesEnabled : bool
* visible : bool
* whatsThis : QString
* width : const int
* windowFilePath : QString
* windowFlags : Qt::WindowFlags
* windowIcon : QIcon
* windowModality : Qt::WindowModality
* windowModified : bool
* windowOpacity : double
* windowTitle : QString
* x : const int
* y : const int

## Public Functions 예제
bool	acceptDrops() const
QString	accessibleDescription() const
QString	accessibleName() const
QList<QAction *>	actions() const
void	activateWindow()
void	addAction(QAction *action)
void	addActions(QList<QAction *> actions)
void	adjustSize()
bool	autoFillBackground() const
QPalette::ColorRole	backgroundRole() const
QBackingStore *	backingStore() const
QSize	baseSize() const
QWidget *	childAt(int x, int y) const
QWidget *	childAt(const QPoint &p) const
QRect	childrenRect() const
QRegion	childrenRegion() const
void	clearFocus()
void	clearMask()
QMargins	contentsMargins() const
QRect	contentsRect() const
Qt::ContextMenuPolicy	contextMenuPolicy() const
QCursor	cursor() const
WId	effectiveWinId() const
void	ensurePolished() const
Qt::FocusPolicy	focusPolicy() const
QWidget *	focusProxy() const
QWidget *	focusWidget() const
const QFont &	font() const
QFontInfo	fontInfo() const
QFontMetrics	fontMetrics() const
QPalette::ColorRole	foregroundRole() const
QRect	frameGeometry() const
QSize	frameSize() const
const QRect &	geometry() const
void	getContentsMargins(int *left, int *top, int *right, int *bottom) const
QPixmap	grab(const QRect &rectangle = QRect( QPoint( 0, 0 ), QSize( -1, -1 ) ))
void	grabGesture(Qt::GestureType gesture, Qt::GestureFlags flags = Qt::GestureFlags())
void	grabKeyboard()
void	grabMouse()
void	grabMouse(const QCursor &cursor)
int	grabShortcut(const QKeySequence &key, Qt::ShortcutContext context = Qt::WindowShortcut)
QGraphicsEffect *	graphicsEffect() const
QGraphicsProxyWidget *	graphicsProxyWidget() const
bool	hasEditFocus() const
bool	hasFocus() const
virtual bool	hasHeightForWidth() const
bool	hasMouseTracking() const
int	height() const
virtual int	heightForWidth(int w) const
Qt::InputMethodHints	inputMethodHints() const
virtual QVariant	inputMethodQuery(Qt::InputMethodQuery query) const
void	insertAction(QAction *before, QAction *action)
void	insertActions(QAction *before, QList<QAction *> actions)
bool	isActiveWindow() const
bool	isAncestorOf(const QWidget *child) const
bool	isEnabled() const
bool	isEnabledTo(const QWidget *ancestor) const
bool	isFullScreen() const
bool	isHidden() const
bool	isMaximized() const
bool	isMinimized() const
bool	isModal() const
bool	isVisible() const
bool	isVisibleTo(const QWidget *ancestor) const
bool	isWindow() const
bool	isWindowModified() const
QLayout *	layout() const
Qt::LayoutDirection	layoutDirection() const
QLocale	locale() const
QPoint	mapFrom(const QWidget *parent, const QPoint &pos) const
QPoint	mapFromGlobal(const QPoint &pos) const
QPoint	mapFromParent(const QPoint &pos) const
QPoint	mapTo(const QWidget *parent, const QPoint &pos) const
QPoint	mapToGlobal(const QPoint &pos) const
QPoint	mapToParent(const QPoint &pos) const
QRegion	mask() const
int	maximumHeight() const
QSize	maximumSize() const
int	maximumWidth() const
int	minimumHeight() const
QSize	minimumSize() const
virtual QSize	minimumSizeHint() const
int	minimumWidth() const
void	move(const QPoint &)
void	move(int x, int y)
QWidget *	nativeParentWidget() const
QWidget *	nextInFocusChain() const
QRect	normalGeometry() const
void	overrideWindowFlags(Qt::WindowFlags flags)
const QPalette &	palette() const
QWidget *	parentWidget() const
QPoint	pos() const
QWidget *	previousInFocusChain() const
QRect	rect() const
void	releaseKeyboard()
void	releaseMouse()
void	releaseShortcut(int id)
void	removeAction(QAction *action)
void	render(QPaintDevice *target, const QPoint &targetOffset = QPoint(), const QRegion &sourceRegion = QRegion(), RenderFlags renderFlags = RenderFlags( DrawWindowBackground | DrawChildren ))
void	render(QPainter *painter, const QPoint &targetOffset = QPoint(), const QRegion &sourceRegion = QRegion(), RenderFlags renderFlags = RenderFlags( DrawWindowBackground | DrawChildren ))
void	repaint(int x, int y, int w, int h)
void	repaint(const QRect &rect)
void	repaint(const QRegion &rgn)
void	resize(const QSize &)
void	resize(int w, int h)
bool	restoreGeometry(const QByteArray &geometry)
QByteArray	saveGeometry() const
void	scroll(int dx, int dy)
void	scroll(int dx, int dy, const QRect &r)
void	setAcceptDrops(bool on)
void	setAccessibleDescription(const QString &description)
void	setAccessibleName(const QString &name)
void	setAttribute(Qt::WidgetAttribute attribute, bool on = true)
void	setAutoFillBackground(bool enabled)
void	setBackgroundRole(QPalette::ColorRole role)
void	setBaseSize(const QSize &)
void	setBaseSize(int basew, int baseh)
void	setContentsMargins(int left, int top, int right, int bottom)
void	setContentsMargins(const QMargins &margins)
void	setContextMenuPolicy(Qt::ContextMenuPolicy policy)
void	setCursor(const QCursor &)
void	setEditFocus(bool enable)
void	setFixedHeight(int h)
void	setFixedSize(const QSize &s)
void	setFixedSize(int w, int h)
void	setFixedWidth(int w)
void	setFocus(Qt::FocusReason reason)
void	setFocusPolicy(Qt::FocusPolicy policy)
void	setFocusProxy(QWidget *w)
void	setFont(const QFont &)
void	setForegroundRole(QPalette::ColorRole role)
void	setGeometry(const QRect &)
void	setGeometry(int x, int y, int w, int h)
void	setGraphicsEffect(QGraphicsEffect *effect)
void	setInputMethodHints(Qt::InputMethodHints hints)
void	setLayout(QLayout *layout)
void	setLayoutDirection(Qt::LayoutDirection direction)
void	setLocale(const QLocale &locale)
void	setMask(const QBitmap &bitmap)
void	setMask(const QRegion &region)
void	setMaximumHeight(int maxh)
void	setMaximumSize(const QSize &)
void	setMaximumSize(int maxw, int maxh)
void	setMaximumWidth(int maxw)
void	setMinimumHeight(int minh)
void	setMinimumSize(const QSize &)
void	setMinimumSize(int minw, int minh)
void	setMinimumWidth(int minw)
void	setMouseTracking(bool enable)
void	setPalette(const QPalette &)
void	setParent(QWidget *parent)
void	setParent(QWidget *parent, Qt::WindowFlags f)
void	setShortcutAutoRepeat(int id, bool enable = true)
void	setShortcutEnabled(int id, bool enable = true)
void	setSizeIncrement(const QSize &)
void	setSizeIncrement(int w, int h)
void	setSizePolicy(QSizePolicy)
void	setSizePolicy(QSizePolicy::Policy horizontal, QSizePolicy::Policy vertical)
void	setStatusTip(const QString &)
void	setStyle(QStyle *style)
void	setToolTip(const QString &)
void	setToolTipDuration(int msec)
void	setUpdatesEnabled(bool enable)
void	setWhatsThis(const QString &)
void	setWindowFilePath(const QString &filePath)
void	setWindowFlags(Qt::WindowFlags type)
void	setWindowIcon(const QIcon &icon)
void	setWindowModality(Qt::WindowModality windowModality)
void	setWindowOpacity(qreal level)
void	setWindowRole(const QString &role)
void	setWindowState(Qt::WindowStates windowState)
void	setupUi(QWidget *widget)
QSize	size() const
virtual QSize	sizeHint() const
QSize	sizeIncrement() const
QSizePolicy	sizePolicy() const
void	stackUnder(QWidget *w)
QString	statusTip() const
QStyle *	style() const
QString	styleSheet() const
bool	testAttribute(Qt::WidgetAttribute attribute) const
QString	toolTip() const
int	toolTipDuration() const
bool	underMouse() const
void	ungrabGesture(Qt::GestureType gesture)
void	unsetCursor()
void	unsetLayoutDirection()
void	unsetLocale()
void	update(int x, int y, int w, int h)
void	update(const QRect &rect)
void	update(const QRegion &rgn)
void	updateGeometry()
bool	updatesEnabled() const
QRegion	visibleRegion() const
QString	whatsThis() const
int	width() const
WId	winId() const
QWidget *	window() const
QString	windowFilePath() const
Qt::WindowFlags	windowFlags() const
QWindow *	windowHandle() const
QIcon	windowIcon() const
Qt::WindowModality	windowModality() const
qreal	windowOpacity() const
QString	windowRole() const
Qt::WindowStates	windowState() const
QString	windowTitle() const
Qt::WindowType	windowType() const
int	x() const
int	y() const

## Public Slots
bool	close()
void	hide()
void	lower()
void	raise()
void	repaint()
void	setDisabled(bool disable)
void	setEnabled(bool)
void	setFocus()
void	setHidden(bool hidden)
void	setStyleSheet(const QString &styleSheet)
virtual void	setVisible(bool visible)
void	setWindowModified(bool)
void	setWindowTitle(const QString &)
void	show()
void	showFullScreen()
void	showMaximized()
void	showMinimized()
void	showNormal()
void	update()