
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module devices</title>
<meta charset="utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>devices</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/home/pi/github-repo/raspberry-pi-device-library/rpi_devices/devices.py">/home/pi/github-repo/raspberry-pi-device-library/rpi_devices/devices.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="RPi.GPIO.html">RPi.GPIO</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="__builtin__.html#object">__builtin__.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="devices.html#DCMotor">DCMotor</a>
</font></dt><dt><font face="helvetica, arial"><a href="devices.html#LED">LED</a>
</font></dt><dt><font face="helvetica, arial"><a href="devices.html#Servo">Servo</a>
</font></dt><dt><font face="helvetica, arial"><a href="devices.html#SimpleMotor">SimpleMotor</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="DCMotor">class <strong>DCMotor</strong></a>(<a href="__builtin__.html#object">__builtin__.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt>DC&nbsp;Motor&nbsp;which&nbsp;is&nbsp;connected&nbsp;to&nbsp;a&nbsp;controller&nbsp;(L293D&nbsp;or&nbsp;similar)<br>
&nbsp;<br>
Use&nbsp;this&nbsp;class&nbsp;for&nbsp;a&nbsp;DC&nbsp;motor&nbsp;whose&nbsp;rotation&nbsp;speed&nbsp;needs&nbsp;to&nbsp;be&nbsp;controlled.<br>
Typically,&nbsp;the&nbsp;Pi's&nbsp;GPIO&nbsp;will&nbsp;be&nbsp;connected&nbsp;to&nbsp;the&nbsp;pins&nbsp;of&nbsp;a&nbsp;L293D&nbsp;or&nbsp;similar&nbsp;controller,<br>
and&nbsp;the&nbsp;controller&nbsp;is&nbsp;connected&nbsp;to&nbsp;the&nbsp;motor.<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="DCMotor-__init__"><strong>__init__</strong></a>(self, a, b, en, mode<font color="#909090">=10</font>)</dt><dd><tt>Construct&nbsp;a&nbsp;new&nbsp;'<a href="#DCMotor">DCMotor</a>'&nbsp;<a href="__builtin__.html#object">object</a>.<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;a:&nbsp;GPIO&nbsp;pin&nbsp;number&nbsp;connected&nbsp;to&nbsp;A&nbsp;pin&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;b:&nbsp;GPIO&nbsp;pin&nbsp;number&nbsp;connected&nbsp;to&nbsp;B&nbsp;pin&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;en:&nbsp;GPIO&nbsp;pin&nbsp;number&nbsp;connected&nbsp;to&nbsp;the&nbsp;EN&nbsp;pin&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;mode:&nbsp;GPIO&nbsp;pin&nbsp;numbering&nbsp;mode,&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD&nbsp;(default)<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;mode&nbsp;is&nbsp;not&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD</tt></dd></dl>

<dl><dt><a name="DCMotor-backward"><strong>backward</strong></a>(self, dc)</dt><dd><tt>Rotates&nbsp;the&nbsp;motor&nbsp;in&nbsp;an&nbsp;arbitrary&nbsp;direction.<br>
&nbsp;<br>
The&nbsp;directions&nbsp;depend&nbsp;on&nbsp;the&nbsp;circuit&nbsp;connections&nbsp;and&nbsp;so&nbsp;cannot&nbsp;be&nbsp;guaranteed.<br>
Only&nbsp;guarantee&nbsp;is&nbsp;that&nbsp;forward&nbsp;and&nbsp;backward&nbsp;methods&nbsp;will&nbsp;always&nbsp;rotate&nbsp;in&nbsp;opposite&nbsp;directions.</tt></dd></dl>

<dl><dt><a name="DCMotor-change_speed"><strong>change_speed</strong></a>(self, dc)</dt><dd><tt>Changes&nbsp;the&nbsp;speed&nbsp;of&nbsp;rotation&nbsp;of&nbsp;motor.<br>
&nbsp;<br>
Manipulates&nbsp;the&nbsp;duty&nbsp;cycle&nbsp;of&nbsp;the&nbsp;internal&nbsp;software&nbsp;PWM&nbsp;to&nbsp;change&nbsp;the&nbsp;rotation&nbsp;speed.<br>
Higher&nbsp;the&nbsp;duty&nbsp;cycle,&nbsp;faster&nbsp;the&nbsp;speed&nbsp;of&nbsp;rotation.<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;dc:&nbsp;Duty&nbsp;cycle&nbsp;to&nbsp;change&nbsp;to<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;0&nbsp;&lt;=&nbsp;dc&nbsp;&lt;=&nbsp;100&nbsp;is&nbsp;not&nbsp;True</tt></dd></dl>

<dl><dt><a name="DCMotor-forward"><strong>forward</strong></a>(self, dc)</dt><dd><tt>Rotates&nbsp;the&nbsp;motor&nbsp;in&nbsp;an&nbsp;arbitrary&nbsp;direction.<br>
&nbsp;<br>
The&nbsp;directions&nbsp;depend&nbsp;on&nbsp;the&nbsp;circuit&nbsp;connections&nbsp;and&nbsp;so&nbsp;cannot&nbsp;be&nbsp;guaranteed.<br>
Only&nbsp;guarantee&nbsp;is&nbsp;that&nbsp;forward&nbsp;and&nbsp;backward&nbsp;methods&nbsp;will&nbsp;always&nbsp;rotate&nbsp;in&nbsp;opposite&nbsp;directions.</tt></dd></dl>

<dl><dt><a name="DCMotor-get_settings"><strong>get_settings</strong></a>(self)</dt><dd><tt>Returns&nbsp;a&nbsp;dictionary&nbsp;of&nbsp;GPIO&nbsp;pins&nbsp;being&nbsp;used&nbsp;and&nbsp;the&nbsp;mode&nbsp;of&nbsp;setup<br>
&nbsp;<br>
Dictionary&nbsp;contains&nbsp;the&nbsp;following&nbsp;keys:<br>
&nbsp;&nbsp;&nbsp;&nbsp;MODE:&nbsp;Mode&nbsp;being&nbsp;used&nbsp;by&nbsp;the&nbsp;<a href="__builtin__.html#object">object</a>&nbsp;as&nbsp;string<br>
&nbsp;&nbsp;&nbsp;&nbsp;A:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;pin&nbsp;A&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;B:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;pin&nbsp;B&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;EN:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;enabler&nbsp;pin&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller</tt></dd></dl>

<dl><dt><a name="DCMotor-stop"><strong>stop</strong></a>(self)</dt><dd><tt>Stops&nbsp;the&nbsp;motor<br>
&nbsp;<br>
This&nbsp;has&nbsp;no&nbsp;effect&nbsp;if&nbsp;motor&nbsp;is&nbsp;not&nbsp;rotating.</tt></dd></dl>

<dl><dt><a name="DCMotor-swap"><strong>swap</strong></a>()</dt><dd><tt>Swap&nbsp;the&nbsp;forward&nbsp;and&nbsp;backward&nbsp;directions<br>
&nbsp;<br>
No&nbsp;need&nbsp;to&nbsp;change&nbsp;any&nbsp;circuit&nbsp;connections</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table> <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="LED">class <strong>LED</strong></a>(<a href="__builtin__.html#object">__builtin__.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt>Light&nbsp;Emitting&nbsp;Diode&nbsp;attached&nbsp;to&nbsp;the&nbsp;Pi<br>
&nbsp;<br>
Use&nbsp;this&nbsp;class&nbsp;for&nbsp;LEDs,&nbsp;Laser&nbsp;Diodes&nbsp;or&nbsp;any&nbsp;other&nbsp;single&nbsp;pin&nbsp;controlled&nbsp;device&nbsp;for&nbsp;which<br>
the&nbsp;methods&nbsp;provided&nbsp;make&nbsp;sense<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="LED-__init__"><strong>__init__</strong></a>(self, pin, mode<font color="#909090">=10</font>)</dt><dd><tt>Constructs&nbsp;a&nbsp;<a href="#LED">LED</a>&nbsp;<a href="__builtin__.html#object">object</a><br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;pin:&nbsp;GPIO&nbsp;pin&nbsp;of&nbsp;the&nbsp;Pi&nbsp;connected&nbsp;to&nbsp;diode<br>
&nbsp;&nbsp;&nbsp;&nbsp;mode:&nbsp;GPIO&nbsp;pin&nbsp;numbering&nbsp;mode,&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD&nbsp;(default)<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;mode&nbsp;is&nbsp;not&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD</tt></dd></dl>

<dl><dt><a name="LED-blink"><strong>blink</strong></a>(self, blinks, duration<font color="#909090">=0.1</font>, interval<font color="#909090">=0.1</font>)</dt><dd><tt>Blinks&nbsp;the&nbsp;<a href="#LED">LED</a>&nbsp;for&nbsp;specified&nbsp;number&nbsp;of&nbsp;times<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;blinks:&nbsp;Number&nbsp;of&nbsp;time&nbsp;the&nbsp;<a href="#LED">LED</a>&nbsp;will&nbsp;go&nbsp;on&nbsp;and&nbsp;off<br>
&nbsp;&nbsp;&nbsp;&nbsp;duration:&nbsp;Duration&nbsp;in&nbsp;seconds&nbsp;for&nbsp;the&nbsp;<a href="#LED">LED</a>&nbsp;to&nbsp;stay&nbsp;on&nbsp;(default:&nbsp;0.1&nbsp;seconds)<br>
&nbsp;&nbsp;&nbsp;&nbsp;interval:&nbsp;Interval&nbsp;in&nbsp;seconds&nbsp;between&nbsp;<a href="#LED">LED</a>&nbsp;turning&nbsp;off&nbsp;and&nbsp;turning&nbsp;back&nbsp;on&nbsp;(default:&nbsp;0.1&nbsp;seconds)</tt></dd></dl>

<dl><dt><a name="LED-flash"><strong>flash</strong></a>(self, duration<font color="#909090">=0.01</font>)</dt><dd><tt>Flashes&nbsp;the&nbsp;<a href="#LED">LED</a>&nbsp;once<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;duration:&nbsp;Duration&nbsp;of&nbsp;the&nbsp;flash&nbsp;in&nbsp;seconds&nbsp;(default:&nbsp;0.01&nbsp;seconds)</tt></dd></dl>

<dl><dt><a name="LED-get_settings"><strong>get_settings</strong></a>()</dt><dd><tt>Returns&nbsp;a&nbsp;dictionary&nbsp;of&nbsp;the&nbsp;pin&nbsp;and&nbsp;mode&nbsp;of&nbsp;the&nbsp;<a href="#LED">LED</a><br>
&nbsp;<br>
Dictionary&nbsp;contains&nbsp;the&nbsp;following&nbsp;keys:<br>
&nbsp;&nbsp;&nbsp;&nbsp;MODE:&nbsp;Mode&nbsp;being&nbsp;used&nbsp;by&nbsp;the&nbsp;<a href="__builtin__.html#object">object</a>&nbsp;as&nbsp;string<br>
&nbsp;&nbsp;&nbsp;&nbsp;P:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;the&nbsp;<a href="#LED">LED</a></tt></dd></dl>

<dl><dt><a name="LED-off"><strong>off</strong></a>(self)</dt><dd><tt>Turns&nbsp;off&nbsp;the&nbsp;<a href="#LED">LED</a></tt></dd></dl>

<dl><dt><a name="LED-on"><strong>on</strong></a>(self)</dt><dd><tt>Turns&nbsp;on&nbsp;the&nbsp;<a href="#LED">LED</a></tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table> <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="Servo">class <strong>Servo</strong></a>(<a href="__builtin__.html#object">__builtin__.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt><a href="#Servo">Servo</a>&nbsp;motor&nbsp;<br>
&nbsp;<br>
Use&nbsp;this&nbsp;<a href="__builtin__.html#object">object</a>&nbsp;for&nbsp;a&nbsp;servo&nbsp;connected&nbsp;to&nbsp;the&nbsp;Raspberry&nbsp;Pi<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="Servo-__init__"><strong>__init__</strong></a>(self, p, mode<font color="#909090">=10</font>, freq<font color="#909090">=50</font>, zero<font color="#909090">=3</font>, slope<font color="#909090">=0.04722</font>, lower<font color="#909090">=0</font>, upper<font color="#909090">=360</font>)</dt><dd><tt>Construct&nbsp;a&nbsp;new&nbsp;<a href="#Servo">Servo</a>&nbsp;<a href="__builtin__.html#object">object</a><br>
&nbsp;<br>
For&nbsp;most&nbsp;standard&nbsp;servos,&nbsp;the&nbsp;default&nbsp;inputs&nbsp;will&nbsp;work,&nbsp;except&nbsp;when&nbsp;0&nbsp;postion&nbsp;needs&nbsp;to<br>
be&nbsp;changed&nbsp;or&nbsp;a&nbsp;specific&nbsp;PWM&nbsp;frequency&nbsp;is&nbsp;required<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;p:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;the&nbsp;control&nbsp;pin&nbsp;of&nbsp;the&nbsp;servo<br>
&nbsp;&nbsp;&nbsp;&nbsp;mode:&nbsp;GPIO&nbsp;pin&nbsp;numbering&nbsp;mode,&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD&nbsp;(default)<br>
&nbsp;&nbsp;&nbsp;&nbsp;freq:&nbsp;Frequency&nbsp;of&nbsp;internal&nbsp;PWM&nbsp;(default:&nbsp;50)<br>
&nbsp;&nbsp;&nbsp;&nbsp;zero:&nbsp;Zero&nbsp;degree&nbsp;position&nbsp;duty&nbsp;cycle&nbsp;(default:&nbsp;3)<br>
&nbsp;&nbsp;&nbsp;&nbsp;slope:&nbsp;Slope&nbsp;of&nbsp;the&nbsp;function&nbsp;that&nbsp;translates&nbsp;duty&nbsp;cycles&nbsp;to&nbsp;position&nbsp;(default:&nbsp;0.04722)<br>
&nbsp;&nbsp;&nbsp;&nbsp;lower:&nbsp;Lower&nbsp;limit&nbsp;on&nbsp;the&nbsp;position&nbsp;of&nbsp;servo&nbsp;in&nbsp;degrees&nbsp;(default:&nbsp;0)<br>
&nbsp;&nbsp;&nbsp;&nbsp;upper:&nbsp;Upper&nbsp;limit&nbsp;on&nbsp;the&nbsp;position&nbsp;of&nbsp;servo&nbsp;in&nbsp;degrees&nbsp;(default:&nbsp;360)<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;mode&nbsp;is&nbsp;not&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD&nbsp;or&nbsp;lower&nbsp;and&nbsp;upper&nbsp;values&nbsp;don't&nbsp;make&nbsp;sense</tt></dd></dl>

<dl><dt><a name="Servo-change_duty_cycle"><strong>change_duty_cycle</strong></a>(self, dc)</dt><dd><tt>Changes&nbsp;the&nbsp;duty&nbsp;cycle&nbsp;of&nbsp;the&nbsp;internal&nbsp;PWM<br>
&nbsp;<br>
Also&nbsp;sets&nbsp;the&nbsp;servo&nbsp;to&nbsp;the&nbsp;position&nbsp;for&nbsp;that&nbsp;duty&nbsp;cycle<br>
Can&nbsp;be&nbsp;used&nbsp;for&nbsp;obtaining&nbsp;d0&nbsp;and&nbsp;d180&nbsp;for&nbsp;the&nbsp;config&nbsp;method<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;dc:&nbsp;New&nbsp;duty&nbsp;cycle&nbsp;of&nbsp;the&nbsp;internal&nbsp;PWM<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;duty&nbsp;cycle&nbsp;is&nbsp;not&nbsp;between&nbsp;0&nbsp;and&nbsp;100,&nbsp;both&nbsp;inclusive</tt></dd></dl>

<dl><dt><a name="Servo-change_freq"><strong>change_freq</strong></a>(self, freq)</dt><dd><tt>Changes&nbsp;the&nbsp;frequency&nbsp;of&nbsp;the&nbsp;internal&nbsp;PWM<br>
&nbsp;<br>
After&nbsp;this,&nbsp;the&nbsp;servo&nbsp;will&nbsp;probably&nbsp;need&nbsp;to&nbsp;be&nbsp;reconfigured&nbsp;using&nbsp;config&nbsp;method<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;freq:&nbsp;The&nbsp;new&nbsp;frequency&nbsp;for&nbsp;the&nbsp;internal&nbsp;PWM<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;frequency&nbsp;is&nbsp;negative&nbsp;or&nbsp;zero</tt></dd></dl>

<dl><dt><a name="Servo-change_restrictions"><strong>change_restrictions</strong></a>(self, lower, upper)</dt><dd><tt>Changes&nbsp;the&nbsp;limits&nbsp;between&nbsp;which&nbsp;the&nbsp;servo&nbsp;can&nbsp;be&nbsp;set<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;lower:&nbsp;Lower&nbsp;limit&nbsp;on&nbsp;the&nbsp;position&nbsp;of&nbsp;servo&nbsp;in&nbsp;degrees<br>
&nbsp;&nbsp;&nbsp;&nbsp;upper:&nbsp;Upper&nbsp;limit&nbsp;on&nbsp;the&nbsp;position&nbsp;of&nbsp;servo&nbsp;in&nbsp;degrees&nbsp;<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;lower&nbsp;and&nbsp;upper&nbsp;values&nbsp;don't&nbsp;make&nbsp;sense</tt></dd></dl>

<dl><dt><a name="Servo-config"><strong>config</strong></a>(self, d0, d180)</dt><dd><tt>Configure&nbsp;the&nbsp;servo&nbsp;positions<br>
&nbsp;<br>
Resets&nbsp;the&nbsp;0&nbsp;position&nbsp;of&nbsp;servo&nbsp;and&nbsp;the&nbsp;recalculates&nbsp;the&nbsp;slope<br>
Note&nbsp;that&nbsp;there&nbsp;is&nbsp;no&nbsp;way&nbsp;to&nbsp;confirm&nbsp;the&nbsp;actual&nbsp;positions&nbsp;of&nbsp;the&nbsp;servo,<br>
so&nbsp;passing&nbsp;bad&nbsp;inputs&nbsp;to&nbsp;this&nbsp;can&nbsp;lead&nbsp;to&nbsp;undefined&nbsp;behavior&nbsp;of&nbsp;turn&nbsp;method<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;d0:&nbsp;New&nbsp;0&nbsp;degree&nbsp;position&nbsp;duty&nbsp;cycle<br>
&nbsp;&nbsp;&nbsp;&nbsp;d180:&nbsp;New&nbsp;180&nbsp;degree&nbsp;position&nbsp;duty&nbsp;cycle<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;d180&nbsp;&lt;&nbsp;d0&nbsp;or&nbsp;either&nbsp;value&nbsp;is&nbsp;negative&nbsp;or&nbsp;zero</tt></dd></dl>

<dl><dt><a name="Servo-get_settings"><strong>get_settings</strong></a>(self)</dt><dd><tt>Returns&nbsp;a&nbsp;dictionary&nbsp;of&nbsp;the&nbsp;settings&nbsp;of&nbsp;the&nbsp;servo<br>
&nbsp;<br>
Dictionary&nbsp;contains&nbsp;the&nbsp;following&nbsp;keys:<br>
&nbsp;&nbsp;&nbsp;&nbsp;MODE:&nbsp;Mode&nbsp;being&nbsp;used&nbsp;by&nbsp;the&nbsp;<a href="__builtin__.html#object">object</a>&nbsp;as&nbsp;string<br>
&nbsp;&nbsp;&nbsp;&nbsp;P:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;the&nbsp;control&nbsp;pin&nbsp;of&nbsp;the&nbsp;servo<br>
&nbsp;&nbsp;&nbsp;&nbsp;LOWER:&nbsp;Lower&nbsp;limit&nbsp;on&nbsp;the&nbsp;position&nbsp;of&nbsp;the&nbsp;servo&nbsp;in&nbsp;degrees<br>
&nbsp;&nbsp;&nbsp;&nbsp;UPPER:&nbsp;Upper&nbsp;limit&nbsp;on&nbsp;the&nbsp;position&nbsp;of&nbsp;the&nbsp;servo&nbsp;in&nbsp;degrees</tt></dd></dl>

<dl><dt><a name="Servo-turn"><strong>turn</strong></a>(self, angle)</dt><dd><tt>Turn&nbsp;the&nbsp;servo&nbsp;to&nbsp;the&nbsp;specified&nbsp;angle<br>
&nbsp;<br>
If&nbsp;angle&nbsp;is&nbsp;not&nbsp;between&nbsp;the&nbsp;limits&nbsp;set&nbsp;during&nbsp;construction&nbsp;or&nbsp;using&nbsp;change_restrictions&nbsp;later,<br>
servo&nbsp;is&nbsp;set&nbsp;to&nbsp;closest&nbsp;limit&nbsp;position<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;angle:&nbsp;Angle&nbsp;of&nbsp;desired&nbsp;position&nbsp;of&nbsp;the&nbsp;servo</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table> <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="SimpleMotor">class <strong>SimpleMotor</strong></a>(<a href="__builtin__.html#object">__builtin__.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt>DC&nbsp;motor&nbsp;which&nbsp;does&nbsp;not&nbsp;require&nbsp;speed&nbsp;control<br>
&nbsp;<br>
Use&nbsp;this&nbsp;<a href="__builtin__.html#object">object</a>&nbsp;for&nbsp;a&nbsp;DC&nbsp;motor&nbsp;which&nbsp;does&nbsp;not&nbsp;need&nbsp;to&nbsp;be&nbsp;controlled<br>
using&nbsp;PWM<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="SimpleMotor-__init__"><strong>__init__</strong></a>(self, a, b, mode<font color="#909090">=10</font>)</dt><dd><tt>Construct&nbsp;a&nbsp;new&nbsp;'<a href="#DCMotor">DCMotor</a>'&nbsp;<a href="__builtin__.html#object">object</a>.<br>
&nbsp;<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;a:&nbsp;GPIO&nbsp;pin&nbsp;number&nbsp;connected&nbsp;to&nbsp;one&nbsp;of&nbsp;the&nbsp;motor&nbsp;pins,&nbsp;directly&nbsp;or&nbsp;via&nbsp;a&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;b:&nbsp;GPIO&nbsp;pin&nbsp;number&nbsp;connected&nbsp;to&nbsp;the&nbsp;other&nbsp;motor&nbsp;pin,&nbsp;directly&nbsp;or&nbsp;via&nbsp;a&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;mode:&nbsp;GPIO&nbsp;pin&nbsp;numbering&nbsp;mode,&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD&nbsp;(default)<br>
&nbsp;<br>
Raises:<br>
&nbsp;&nbsp;&nbsp;&nbsp;ValueError:&nbsp;If&nbsp;mode&nbsp;is&nbsp;not&nbsp;RPi.GPIO.BCM&nbsp;or&nbsp;RPi.GPIO.BOARD</tt></dd></dl>

<dl><dt><a name="SimpleMotor-backward"><strong>backward</strong></a>(self)</dt><dd><tt>Rotates&nbsp;the&nbsp;motor&nbsp;in&nbsp;an&nbsp;arbitrary&nbsp;direction.<br>
&nbsp;<br>
The&nbsp;directions&nbsp;depend&nbsp;on&nbsp;the&nbsp;circuit&nbsp;connections&nbsp;and&nbsp;so&nbsp;cannot&nbsp;be&nbsp;guaranteed.<br>
Only&nbsp;guarantee&nbsp;is&nbsp;that&nbsp;forward&nbsp;and&nbsp;backward&nbsp;methods&nbsp;will&nbsp;always&nbsp;rotate&nbsp;in&nbsp;opposite&nbsp;directions.</tt></dd></dl>

<dl><dt><a name="SimpleMotor-forward"><strong>forward</strong></a>(self)</dt><dd><tt>Rotates&nbsp;the&nbsp;motor&nbsp;in&nbsp;an&nbsp;arbitrary&nbsp;direction.<br>
&nbsp;<br>
The&nbsp;directions&nbsp;depend&nbsp;on&nbsp;the&nbsp;circuit&nbsp;connections&nbsp;and&nbsp;so&nbsp;cannot&nbsp;be&nbsp;guaranteed.<br>
Only&nbsp;guarantee&nbsp;is&nbsp;that&nbsp;forward&nbsp;and&nbsp;backward&nbsp;methods&nbsp;will&nbsp;always&nbsp;rotate&nbsp;in&nbsp;opposite&nbsp;directions.</tt></dd></dl>

<dl><dt><a name="SimpleMotor-get_settings"><strong>get_settings</strong></a>(self)</dt><dd><tt>Returns&nbsp;a&nbsp;dictionary&nbsp;of&nbsp;GPIO&nbsp;pins&nbsp;being&nbsp;used&nbsp;and&nbsp;the&nbsp;mode&nbsp;of&nbsp;setup<br>
&nbsp;<br>
Dictionary&nbsp;contains&nbsp;the&nbsp;following&nbsp;keys:<br>
&nbsp;&nbsp;&nbsp;&nbsp;MODE:&nbsp;Mode&nbsp;being&nbsp;used&nbsp;by&nbsp;the&nbsp;<a href="__builtin__.html#object">object</a>&nbsp;as&nbsp;string<br>
&nbsp;&nbsp;&nbsp;&nbsp;A:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;pin&nbsp;A&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller<br>
&nbsp;&nbsp;&nbsp;&nbsp;B:&nbsp;GPIO&nbsp;pin&nbsp;connected&nbsp;to&nbsp;pin&nbsp;B&nbsp;of&nbsp;the&nbsp;motor&nbsp;controller</tt></dd></dl>

<dl><dt><a name="SimpleMotor-stop"><strong>stop</strong></a>(self)</dt><dd><tt>Stops&nbsp;the&nbsp;motor<br>
&nbsp;<br>
This&nbsp;has&nbsp;no&nbsp;effect&nbsp;if&nbsp;motor&nbsp;is&nbsp;not&nbsp;rotating.</tt></dd></dl>

<dl><dt><a name="SimpleMotor-swap"><strong>swap</strong></a>(self)</dt><dd><tt>Swap&nbsp;the&nbsp;forward&nbsp;and&nbsp;backward&nbsp;directions<br>
&nbsp;<br>
No&nbsp;need&nbsp;to&nbsp;change&nbsp;any&nbsp;circuit&nbsp;connections</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-cleanup"><strong>cleanup</strong></a>()</dt><dd><tt>Same&nbsp;as&nbsp;RPi.GPIO.<a href="#-cleanup">cleanup</a>()</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>__all__</strong> = ['cleanup', 'DCMotor', 'SimpleMotor', 'Servo', 'LED']</td></tr></table>
</body></html>
