<!DOCTYPE html>
<html>

<head>
  <title>Data Structure - 幕布</title>
  <meta charset="utf-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="renderer" content="webkit" />
  <meta name="author" content="mubu.com" />
</head>

<body style="margin: 50px 20px;color: #333;font-family: 'Helvetica Neue','Hiragino Sans GB','WenQuanYi Micro Hei','Microsoft Yahei',sans-serif;">
  <div class="export-wrapper">
    <div style="font-size: 24px; padding: 20px 15px 0;"></div>
    <ul style="list-style: disc outside;">
      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Data Structure</span></span>
        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">python手写&gt; <a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/tobgu/pyrsistent" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/tobgu/pyrsistent</a></span></li>
          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">更快的list &gt; <a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/DanielStutzbach/blist" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/DanielStutzbach/blist</a></span></li>
          <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Linked List:</span></span>
            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">资源：</span></span>
                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">现实运用：</span></span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Consider the history section of web browsers, where it creates a linked list of web-pages visited, so that when you check history (traversal of a list) or press back button, the previous node's data is fetched.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">One common sighted example is&nbsp;low level memory management (i.e. the heap as managed by malloc in C or new in Java, etc) is&nbsp;often implemented as a linked list, with each node representing a used or available (free) block of memory. These blocks may be of any size, change size (combine and split), be freed or assigned in any order, and reordered. A linked list means you can keep track of all of these "nodes" and manipulate them fairly easily.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Also,&nbsp;Hashtables that use chaining&nbsp;to resolve hash collisions typically have one linked list per bucket for the elements in that bucket.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">A simple real life example is a Train, here each coach is connected to its previous and next coach&nbsp;(Except first and last).&nbsp;In terms of programming consider coach body as node value and connectors as links to previous and next nodes.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Our brain is also&nbsp;a good example of&nbsp;linked list. In the initial stages of learning something by heart, the natural process is to link one item to next. It's a subconscious act. Also, when we forget something and try to remember, than our brain follows association and tries to link one memory with another and so on and&nbsp;we finally&nbsp;recall&nbsp;the lost memory.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">E.g. Consider the thinking process when you placed your bike key&nbsp;somewhere and couldn't remember.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Another real life example could a be queue/line of persons&nbsp;standing for food in mess, insertion is done at one end and deletion at other. And these operations happen frequent.&nbsp;dynamic queues / stacks are efficiently implemented using linkedlists.</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">As a&nbsp;practical example,&nbsp; consider following situation.</span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">A company maintains details of customers.&nbsp; A customer X can bring other customers that can joins list of customers just after X.&nbsp; A customer after X can also leave any time.&nbsp; The only operation that company does is print list of all customers.</span></li>
                        </ul>
                      </li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">优势：</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">链接：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays</a></span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">[MUSIC]&nbsp;Why would you want to use a list rather than an array?</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">The big advantage of an array is random access.&nbsp;You can look at any element of the array in the same amount of time.&nbsp;So reading an array is constant time.&nbsp;It's o over one.</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">In a list,&nbsp;you have to walk down the list step by step to get to the element you want.</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">So reading in a list is linear time.&nbsp;It's o of n. On the other hand, inserting or&nbsp;deleting an item in a list, just requires fiddling some object references.&nbsp;So, it's constant time.&nbsp;But inserting or deleting into an array&nbsp;usually means you have to copy all of the following items in the array.&nbsp;Sometimes you have to copy the whole array if you don't have enough space in memory&nbsp;so that's o of n.&nbsp;In general, arrays are faster to read, and lists are faster to write.&nbsp;So you have to pick your data structure carefully depending on what&nbsp;algorithm you're planning on using with it.</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">For example, there was a time when I needed to do a merge sort&nbsp;on a collection of very large objects.</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Merging two arrays means allocating a third array&nbsp;as big as the original two combined, and then copying each object into it.&nbsp;So it's really slow.&nbsp;Merging two lists means walking down the two lists and&nbsp;just fiddling the references as you go.&nbsp;And when you're done you have one big list.&nbsp;So that's really fast.&nbsp;In this case the algorithmic complexity is the same.&nbsp;They're both n log n, like any merge sort.&nbsp;But in practice, the difference in performance was something like 10 or&nbsp;20 times, because copying the objects took such a long time.&nbsp;So using a list was a big win.</span></li>
                        </ul>
                      </li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">劣势：</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">why you should avoid linked lists (video)：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.youtube.com/watch?v=YQs6IC-vgmo" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.youtube.com/watch?v=YQs6IC-vgmo</a></span></li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Jose :</span></span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">链接</span>：<a class="content-link" target="_blank"
                          rel="noreferrer" href="https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/learn/v4/t/lecture/3179596?start=0" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/learn/v4/t/lecture/3179596?start=0</a></span>
                      </li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">定义：&nbsp;</span>A singly linked list, in its
                        simplest form, is a collection of nodes that collectively form a linear sequence. Each Node stores a references to an object that is an element of the sequence, as well as a reference to the next node of the list.</span>
                      </li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Head/Tail:</span>&nbsp;The list instance maintains
                        a member named<span class="bold" style="font-weight: bold;">&nbsp;head&nbsp;</span>that identifies the first node of the list. In some applications another member named<span class="bold" style="font-weight: bold;">&nbsp;tail&nbsp;</span>that
                        identifies the last node of the list. The first and last node of a linked list are known as the head and tail of the list. We can identify the tail as the node having&nbsp;<span class="bold" style="font-weight: bold;">None</span>&nbsp;as
                        its next reference.</span>
                      </li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Traversing:&nbsp;</span>This process is commonly
                        known as<span class="bold" style="font-weight: bold;">traversing</span>&nbsp;the linked list. Because the next referencec of a node can be viewed as a&nbsp;<span class="bold" style="font-weight: bold;">link</span>&nbsp;or
                        <span class="bold" style="font-weight: bold;">pointer</span>&nbsp;to another node, the process of traversing a list is also known as&nbsp;<span class="bold" style="font-weight: bold;">link hopping</span>&nbsp;or&nbsp;<span class="bold"
                          style="font-weight: bold;">pointer hopping</span>.</span>
                      </li>
                      <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">特性：</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Each node is represented as a unique object, with that instance storing a reference to its element and a reference to the next node(or None)</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">An important property of a linked list is that it does not have a predetermined fixed size (python里list类似)</span></li>
                        </ul>
                      </li>
                      <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Insert Head：</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">We create a new node</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Set its element to the new element</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Set its next link to refer to the current head</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">then set the list's head to point to the new node</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A671%2C%22ow%22%3A1079%2C%22oh%22%3A603%2C%22id%22%3A%22353163401832de1%22%2C%22uri%22%3A%22document_image%2F500dede6-cf83-414b-938a-257630d20778-808326.jpg%22%7D%5D" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">例：</span></span>
                            <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/500dede6-cf83-414b-938a-257630d20778-808326.jpg" style="max-width: 720px; width: 671px;" class="attach-img"></div>
                          </li>
                        </ul>
                      </li>
                      <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Insert Tail:</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Create a new node</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Assign its next reference to None</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Set the next reference of the tail to point to this new node</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">then update the tail reference itself to this new node.</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">例：</span>
                            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                              <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A627%2C%22ow%22%3A1076%2C%22oh%22%3A599%2C%22id%22%3A%22165163401a2ef111c-808326%22%2C%22uri%22%3A%22document_image%2Fbd96a624-1991-4b7b-89ff-b681b294a07e-808326.jpg%22%7D%5D"
                                  style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"></span>
                                <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/bd96a624-1991-4b7b-89ff-b681b294a07e-808326.jpg" style="max-width: 720px; width: 627px;" class="attach-img"></div>
                              </li>
                            </ul>
                          </li>
                        </ul>
                      </li>
                      <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Remove Head:</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A666%2C%22ow%22%3A1070%2C%22oh%22%3A599%2C%22id%22%3A%22364163401c90e0153-808326%22%2C%22uri%22%3A%22document_image%2F1ef1c98e-2de3-498a-bf1c-76d98363ff98-808326.jpg%22%7D%5D"
                              style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"></span>
                            <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/1ef1c98e-2de3-498a-bf1c-76d98363ff98-808326.jpg" style="max-width: 720px; width: 666px;" class="attach-img"></div>
                          </li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">CS Doji:</span></span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">链接：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.youtube.com/watch?v=WwfhLC16bis" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.youtube.com/watch?v=WwfhLC16bis</a></span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">基础教学：</span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">基本：</span></span>
                            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                              <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A419%2C%22ow%22%3A513%2C%22oh%22%3A318%2C%22id%22%3A%221d71634078331a189-808326%22%2C%22uri%22%3A%22document_image%2Fe5924ab0-6206-4a0e-8448-6f2dec2ef4a2-808326.jpg%22%7D%5D"
                                  style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"></span>
                                <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/e5924ab0-6206-4a0e-8448-6f2dec2ef4a2-808326.jpg" style="max-width: 720px; width: 419px;" class="attach-img"></div>
                              </li>
                            </ul>
                          </li>
                          <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A483%2C%22ow%22%3A1362%2C%22oh%22%3A1422%2C%22id%22%3A%2223716340766d1d051-808326%22%2C%22uri%22%3A%22document_image%2F5e15dfd9-8407-48de-90a6-5e1a52e3b1b1-808326.jpg%22%7D%5D"
                              style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">代码实现</span></span>
                            <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/5e15dfd9-8407-48de-90a6-5e1a52e3b1b1-808326.jpg" style="max-width: 720px; width: 483px;" class="attach-img"></div>
                          </li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">然后举了个例子</span></li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Code School:</span></span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">链接：</span><a class="content-link" target="_blank"
                          rel="noreferrer" href="https://www.youtube.com/watch?v=NobHlGUjV3g" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.youtube.com/watch?v=NobHlGUjV3g</a></span>
                      </li>
                      <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Linked List Vs. Array：</span></span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Memory</span></span>
                            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                              <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A761%2C%22ow%22%3A1070%2C%22oh%22%3A447%2C%22id%22%3A%221516340994da707e-808326%22%2C%22uri%22%3A%22document_image%2F3117b027-7ff5-4351-bc74-b0c3720b1e2c-808326.jpg%22%7D%5D"
                                  style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Array Memory问题：</span>C/C++里，因为需要提前设置开辟空间，
                                <span class="bold" style="font-weight: bold;">如果要增加已经定义空间的Size，会对底层的Memory造成影响</span>，如图下：</span>
                                <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/3117b027-7ff5-4351-bc74-b0c3720b1e2c-808326.jpg" style="max-width: 720px; width: 761px;" class="attach-img"></div>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">图中array A如果从Size = 4， 也就是16bytes， 增加到Size = 5，就必须在Memory里面开辟出新的 4bytes * 5 = 20 bytes的空间：</span>
                                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                      <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A661%2C%22ow%22%3A693%2C%22oh%22%3A145%2C%22id%22%3A%22342163409c2fe5106-808326%22%2C%22uri%22%3A%22document_image%2F612e2a42-e66c-4ba1-a9ed-d594193b1d3e-808326.jpg%22%7D%5D"
                                          style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"></span>
                                        <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/612e2a42-e66c-4ba1-a9ed-d594193b1d3e-808326.jpg" style="max-width: 720px; width: 661px;" class="attach-img"></div>
                                      </li>
                                    </ul>
                                  </li>
                                </ul>
                              </li>
                              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Linked List Memory</span>操作的优势显现出来了：</span>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Node的Memory随机分配，如果Insert新Node，仅需在Memory开辟新空间，然后把之前的Tail指向这片空间。</span>
                                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                      <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A675%2C%22ow%22%3A1060%2C%22oh%22%3A441%2C%22id%22%3A%22241163409f12260c9-808326%22%2C%22uri%22%3A%22document_image%2Fe622aae1-bd93-4bff-8bd7-79fc535995a5-808326.jpg%22%7D%5D"
                                          style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"></span>
                                        <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/e622aae1-bd93-4bff-8bd7-79fc535995a5-808326.jpg" style="max-width: 720px; width: 675px;" class="attach-img"></div>
                                      </li>
                                    </ul>
                                  </li>
                                </ul>
                              </li>
                            </ul>
                          </li>
                          <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Insertion：</span></span>
                            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Linked List O(1)：但这两个需要讲清楚，因为Insert建立在找到<span class="bold" style="font-weight: bold;">Insertion point</span></span>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="line-height: 22px;"><span class="content mubu-node" images="%5B%7B%22w%22%3A706%2C%22ow%22%3A1068%2C%22oh%22%3A442%2C%22id%22%3A%221f016340b475d7005-808326%22%2C%22uri%22%3A%22document_image%2F4ace6581-765a-4987-b514-1e661ba47798-808326.jpg%22%7D%5D"
                                      style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"></span>
                                    <div style="padding: 3px 0"><img src="https://img.mubu.com/document_image/4ace6581-765a-4987-b514-1e661ba47798-808326.jpg" style="max-width: 720px; width: 706px;" class="attach-img"></div>
                                  </li>
                                </ul>
                              </li>
                              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">所以假如<span class="bold" style="font-weight: bold;">Search也经常使用</span>，Linked List相对Array
                                <span
                                  class="bold" style="font-weight: bold;">并无优势</span>：</span>
                                  <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                    <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Any application where insertions and deletions happen regularly, search is not a regular operation and elements are always traversed one by one.</span></li>
                                  </ul>
                              </li>
                            </ul>
                          </li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">待实现：</span></span>
                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                  <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">代码实现</span></span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">implement (I did with tail pointer &amp; without):</span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">size() - returns number of data elements in list</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">empty() - bool returns true if empty</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">value_at(index) - returns the value of the nth item (starting at 0 for first)</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">push_front(value) - adds an item to the front of the list</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">pop_front() - remove front item and return its value</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">push_back(value) - adds an item at the end</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">pop_back() - removes end item and returns its value</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">front() - get value of front item</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">back() - get value of end item</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">erase(index) - removes node at given index</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">value_n_from_end(n) - returns the value of the node at nth position from the end of the list</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">reverse() - reverses the list</span></li>
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">remove_value(value) - removes the first item in the list with this value</span></li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li class="collapsed" style="line-height: 22px;"><span class="content mubu-node collapsed" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">代码研究：</span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/OmkarPathak/pygorithm/tree/master/pygorithm" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/OmkarPathak/pygorithm/tree/master/pygorithm</a></span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/keon/algorithms" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/keon/algorithms</a></span></li>
                    </ul>
                  </li>
                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">课件准备：</span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">网盘 : /Users/yui/Movies</span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Google University 的LinkedList</span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Linked Lists</span>
                            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                              <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Description:</span>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Singly Linked Lists (video)：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists" style="color: inherit; text-decoration: underline; opacity: 0.6;">https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists</a></span></li>
                                  <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">CS 61B：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0" style="color: inherit; text-decoration: underline; opacity: 0.6;">https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0</a></span></li>
                                </ul>
                              </li>
                              <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Linked List vs Arrays:</span>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Core Linked Lists Vs Arrays：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays</a></span></li>
                                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">In The Real World Linked Lists Vs Arrays (video)：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays</a></span></li>
                                </ul>
                              </li>
                              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Gotcha: you need pointer to pointer knowledge: (for when you pass a pointer to a function that may change the address where that pointer points) This page is just to get a grasp on ptr to ptr. I don't recommend this list traversal style. Readability and maintainability suffer due to cleverness.</span>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Pointers to Pointers：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.eskimo.com/~scs/cclass/int/sx8.html" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.eskimo.com/~scs/cclass/int/sx8.html</a></span></li>
                                </ul>
                              </li>
                              <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Doubly-linked List</span>
                                <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                                  <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">Description (video)：&nbsp;<a class="content-link" target="_blank" rel="noreferrer" href="https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists" style="color: inherit; text-decoration: underline; opacity: 0.6;">https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists</a></span></li>
                                  <li style="color: rgb(160, 160, 160); line-height: 22px;"><span class="content mubu-node finished" style="text-decoration: line-through; line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">No need to implement</span></li>
                                </ul>
                              </li>
                            </ul>
                          </li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">中文资源：</span>
                    <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="http://www.cnblogs.com/absfree/p/5463372.html" style="text-decoration: underline; opacity: 0.6; color: inherit;">http://www.cnblogs.com/absfree/p/5463372.html</a></span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">python没有指针实现原理：<a class="content-link" target="_blank" rel="noreferrer" href="https://www.zhihu.com/question/22680562" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.zhihu.com/question/22680562</a></span></li>
                      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">更多资源：</span>
                        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
                          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://www.google.com/search?ei=ayvxWvqYF6ed0gLTpICQCQ&amp;q=%E9%93%BE%E8%A1%A8+python&amp;oq=%E9%93%BE%E8%A1%A8+python&amp;gs_l=psy-ab.3..0i67k1.340964.343567.0.343861.16.14.1.1.1.0.151.1197.9j4.13.0....0...1c.1j4.64.psy-ab..3.9.727...0j0i12k1j0i4i30k1j0i8i4i30k1j0i13i4i30k1.0.UTydcRNkE4I" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://www.google.com/search?ei=ayvxWvqYF6ed0gLTpICQCQ&amp;q=%E9%93%BE%E8%A1%A8+python&amp;oq=%E9%93%BE%E8%A1%A8+python&amp;gs_l=psy-ab.3..0i67k1.340964.343567.0.343861.16.14.1.1.1.0.151.1197.9j4.13.0....0...1c.1j4.64.psy-ab..3.9.727...0j0i12k1j0i4i30k1j0i8i4i30k1j0i13i4i30k1.0.UTydcRNkE4I</a></span></li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
      <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><span class="bold" style="font-weight: bold;">Algorithm</span></span>
        <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">数据结构和算法的基础实现：</span>
            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/OmkarPathak/pygorithm/tree/master/pygorithm" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/OmkarPathak/pygorithm/tree/master/pygorithm</a></span></li>
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/keon/algorithms" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/keon/algorithms</a></span></li>
            </ul>
          </li>
          <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;">算法总结：</span>
            <ul class="children" style="list-style: disc outside; padding-bottom: 4px;">
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/yangshun/tech-interview-handbook" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/yangshun/tech-interview-handbook</a></span></li>
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/CyC2018/Interview-Notebook" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/CyC2018/Interview-Notebook</a></span></li>
              <li style="line-height: 22px;"><span class="content mubu-node" style="line-height: 22px; min-height: 22px; font-size: 14px; display: inline-block; vertical-align: top;"><a class="content-link" target="_blank" rel="noreferrer" href="https://github.com/jwasham/coding-interview-university" style="text-decoration: underline; opacity: 0.6; color: inherit;">https://github.com/jwasham/coding-interview-university</a></span></li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </div>

</body>

</html>
