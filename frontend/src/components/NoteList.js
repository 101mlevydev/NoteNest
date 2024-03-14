import React from 'react';

const NoteList = ({ notes }) => {
  return (
    <div>
      <h2>Note List</h2>
      <ul>
        {notes.map(note => (
          <li key={note.id}>
            <strong>{note.title}</strong>: {note.content}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NoteList;
