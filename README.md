# Book Library

Written an GET API, in which user can send filters as follows:
1.Book ID numbers specified as Project Gutenberg ID numbers.
2.Language
3.Mime-type
4.Topic - topic should filter on either ‘subject’ or ‘bookshelf’ or both. Case-insensitive partial matches should be supported. e.g. ‘topic=child’ should among others, return books from the bookshelf ‘Children’s Literature’ and from the subject ‘Child education’.
5.Author - Case-insensitive partial matches should be supported.
6.Title - Case-insensitive partial matches should be supported.
7.Multiple filter criteria should be permitted in each API call and multiple filter values should be allowed for each criterion. e.g. an API call should be able to filter on ‘language=en,fr’ and ‘topic=child, infant’.

As response object contains resultant count of books, book title, author's information shelf, subjects,etc

