
[The book of electronics](https://jekahome.github.io/Electronics)

---

### Настройка mdbook

#### Установить mdbook  

```
cargo install mdbook
```

#### Создание новой книги

```
mdbook init book-electronic
```

Files:
- book.toml: настройка книги (например, название, оформление).
- SUMMARY.md: оглавление книги. Ссылки в этом файле указывают на главы и разделы.
- chapter_X.md: файлы глав. Их содержание пишется в формате Markdown.

#### Редактирование книги

Редактирование оглавления:

В файле [src/SUMMARY.md](https://rust-lang.github.io/mdBook/format/summary.html#example) укажите структуру книги. 

Например:

```
# Summary

- [Введение](./intro.md)
- [Первая глава](./chapter_1.md)
    - [Подраздел](./subsection.md)
- [Вторая глава](./chapter_2.md)

```

Добавление новых глав:

Создайте новые файлы Markdown в src/subsection.md и добавьте их в SUMMARY.md

#### [Сборка книги](https://rust-lang.github.io/mdBook/cli/build.html)

```
mdbook clean
mdbook build
```

Книга будет сгенерирована в папке `book/`. Вы можете открыть её с помощью веб-браузера:

```
firefox book/index.html
```


#### Просмотр

Чтобы увидеть изменения в реальном времени при редактировании книги, используйте команду [serve](https://rust-lang.github.io/mdBook/cli/serve.html)

Запустить сервер и открыть в браузере:

```
mdbook serve --open
```

Запустить сервер:

```
mdbook serve
```


[mdBook Markdown](https://rust-lang.github.io/mdBook/format/markdown.html)
 
#### Препроцессоры
https://github.com/rust-lang/mdBook/wiki/Third-party-plugins

`$ cargo install mdbook-katex`

`$ cargo install mdbook-numeq`

`$ cargo install mdbook-mermaid`

`$ cargo install mdbook-admonish`

- **mdbook-katex**: Препроцессор, преобразующий уравнения LaTex в HTML. 
- **mdbook-numeq**: Препроцессор для автоматического нумерованного уравнения и последующего создания ссылки на эти уравнения для использования в формате LaTeX.
- **mdbook-mermaid**: Препроцессор для поддержки диаграмм
- **mdbook-admonish**: Препроцессор добавляет возможность использовать стилизованные блоки с предупреждениями, заметками, советами и другими выделениями.
- **mdbook-embedify**: Препроцессор который позволяет встраивать в книгу приложения, такие как youtube, codepen и некоторые другие.

 
#### Игнорировать вставки

Вы можете сделать это, заключив контент, который вы хотите игнорировать, в два комментария ниже:

```code

<!-- embed ignore begin -->
 

этот блок будет закомментирован

{% embed youtube id="DyTCOwB0DVw" loading="lazy" %}

 
<!-- embed ignore end -->

```