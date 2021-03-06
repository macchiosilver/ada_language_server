------------------------------------------------------------------------------
--                         Language Server Protocol                         --
--                                                                          --
--                     Copyright (C) 2018-2020, AdaCore                     --
--                                                                          --
-- This is free software;  you can redistribute it  and/or modify it  under --
-- terms of the  GNU General Public License as published  by the Free Soft- --
-- ware  Foundation;  either version 3,  or (at your option) any later ver- --
-- sion.  This software is distributed in the hope  that it will be useful, --
-- but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --
-- TABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public --
-- License for  more details.  You should have  received  a copy of the GNU --
-- General  Public  License  distributed  with  this  software;   see  file --
-- COPYING3.  If not, go to http://www.gnu.org/licenses for a complete copy --
-- of the license.                                                          --
------------------------------------------------------------------------------
--
--  This package provides an Ada stream type to serialize Ada object into JSON.
--

private with Ada.Containers.Vectors;
with Ada.Strings.Wide_Unbounded;
with Ada.Streams;

with GNATCOLL.JSON;

package LSP.JSON_Streams is

   type JSON_Stream (Is_Server_Side : Boolean := False) is
     new Ada.Streams.Root_Stream_Type with private;
   --  Stream implemented over JSON document
   --
   --  To support JSON serialization user provides Read/Write streaming
   --  aspects that are aware of JSON_Stream. Simple types use Read/Write
   --  procedures from this package to convert a value to/from simple JSON
   --  value. Compond types use Start_Object/End_Object if they are represented
   --  as JSON object or Start_Array/End_Array if they are implemented as
   --  JSON stream. After starting object or array compound type iterates over
   --  each of its items using corresponding Read/Write aspects for convertion.
   --  To provide property name compound type uses Key procedure before
   --  calling Read/Write. Each item shoud have Read/Write aspect overriden
   --  in the same way.
   --
   --  The Is_Server_Side discriminant can be used to create distinct
   --  representations on client and server sides.

   procedure Start_Object (Self : not null access JSON_Stream'Class);
   --  Start new JSON object during read/write of some compound type

   procedure End_Object (Self : not null access JSON_Stream'Class);
   --  End JSON object during read/write of some compound type

   procedure Start_Array (Self : not null access JSON_Stream'Class);
   --  Start new JSON array during read/write of some compound type

   procedure End_Array (Self : not null access JSON_Stream'Class);
   --  End JSON array during read/write of some compound type

   function End_Of_Array
    (Self : not null access JSON_Stream'Class) return Boolean;
   --  Returns True when there are no array elements to be read.

   procedure Key
    (Self : not null access JSON_Stream'Class;
     Key  : Ada.Strings.Wide_Unbounded.Unbounded_Wide_String);
   --  Specify property name before do convertion of an item nested in an JSON
   --  object

   procedure Key
    (Self : not null access JSON_Stream'Class;
     Key  : Wide_String);
   --  The same but with Wide_String type

   function Get_JSON_Document
    (Self : not null access JSON_Stream'Class)
       return GNATCOLL.JSON.JSON_Array;
   --  Return resulting JSON document after writting to the JSON stream

   procedure Set_JSON_Document
    (Self : not null access JSON_Stream'Class;
     Data : GNATCOLL.JSON.JSON_Array);
   --  Assign JSON document for reading from the stream

   function Read
    (Self : in out JSON_Stream'Class)
       return GNATCOLL.JSON.JSON_Value;
   --  Reads current value and updates stream's position.

   procedure Write
    (Self : in out JSON_Stream'Class;
     Item : GNATCOLL.JSON.JSON_Value);
   --  Writes value into the stream and updates stream's position.

private
   type State_Kinds is (Array_State, Object_State);

   type State (Kind : State_Kinds := Array_State) is record
      case Kind is
         when Array_State =>
            Current_Array : GNATCOLL.JSON.JSON_Array;
            Index         : Positive := 1;

         when Object_State =>
            Current_Object : GNATCOLL.JSON.JSON_Value;
            Key            : Ada.Strings.Wide_Unbounded.Unbounded_Wide_String;
      end case;
   end record;

   package State_Vectors is new Ada.Containers.Vectors (Positive, State);

   type JSON_Stream (Is_Server_Side : Boolean := False) is
     new Ada.Streams.Root_Stream_Type with
   record
      Writable : Boolean := True;  --  True means stream to write
      Current  : State;
      Stack    : State_Vectors.Vector;
   end record;

   overriding procedure Read
     (Stream : in out JSON_Stream;
      Item   : out Ada.Streams.Stream_Element_Array;
      Last   : out Ada.Streams.Stream_Element_Offset);

   overriding procedure Write
     (Stream : in out JSON_Stream;
      Item   : Ada.Streams.Stream_Element_Array);

end LSP.JSON_Streams;
